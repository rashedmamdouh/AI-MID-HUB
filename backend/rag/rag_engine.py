"""
rag_engine.py — RAG Pipeline with Groq (primary) + HuggingFace (fallback)
--------------------------------------------------------------------------
1. Embedder    → sentence-transformers (all-MiniLM-L6-v2)
2. VectorStore → FAISS semantic search
3. LLM Answer  → Groq free API (llama-3.1-8b-instant) — primary
                 HuggingFace Inference Router          — fallback
"""

import os, json, re, requests
import numpy as np
from typing import List, Tuple
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_MODEL   = os.getenv("EMBEDDING_MODEL_NAME", "sentence-transformers/all-MiniLM-L6-v2")
VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH",    "./rag/vector_store/knowledge_base.index")
CHUNKS_STORE_PATH = os.getenv("CHUNKS_STORE_PATH",    "./rag/vector_store/chunks.json")
HF_API_KEY        = os.getenv("HF_API_KEY",  "")
GROQ_API_KEY      = os.getenv("GROQ_API_KEY", "")

HF_MODEL    = "mistralai/Mistral-7B-Instruct-v0.3"
GROQ_MODEL  = "llama-3.1-8b-instant"

TOP_K         = 5
CHUNK_SIZE    = 500
CHUNK_OVERLAP = 100

_GREETINGS = {"hi","hello","hey","howdy","greetings","good morning","good afternoon",
              "good evening","sup","what's up","whats up","hiya"}

_SYSTEM_PROMPT = (
    "You are a helpful, friendly AI medical assistant. "
    "Answer the patient's question clearly and accurately using the provided medical knowledge. "
    "Write in plain, easy-to-understand language. "
    "Be concise but thorough. "
    "Always recommend consulting a doctor for personal medical decisions."
)


# ══════════════════════════════════════════════════════════════════════════
# 1. CHUNKER
# ══════════════════════════════════════════════════════════════════════════
class Chunker:
    def __init__(self, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
        self.chunk_size = chunk_size
        self.overlap    = overlap

    def chunk_text(self, text, metadata=None):
        chunks, start = [], 0
        while start < len(text):
            end   = min(start + self.chunk_size, len(text))
            chunk = text[start:end].strip()
            if chunk:
                chunks.append({"text": chunk, "metadata": metadata or {}})
            start += self.chunk_size - self.overlap
        return chunks

    def chunk_knowledge_base(self, kb):
        all_chunks = []
        for doc in kb:
            meta = {"title": doc.get("title",""), "category": doc.get("category","")}
            all_chunks.extend(self.chunk_text(doc["text"], metadata=meta))
        return all_chunks


# ══════════════════════════════════════════════════════════════════════════
# 2. EMBEDDER
# ══════════════════════════════════════════════════════════════════════════
class Embedder:
    def __init__(self):
        self._model = None

    def _load(self):
        if self._model is None:
            from sentence_transformers import SentenceTransformer
            print(f"[RAG] Loading embedding model: {EMBEDDING_MODEL} ...")
            self._model = SentenceTransformer(EMBEDDING_MODEL)
            print("[RAG] ✓ Embedding model ready")
        return self._model

    def encode(self, texts):
        return self._load().encode(texts, show_progress_bar=False, normalize_embeddings=True)


# ══════════════════════════════════════════════════════════════════════════
# 3. VECTOR STORE
# ══════════════════════════════════════════════════════════════════════════
class VectorStore:
    def __init__(self, embedder):
        self.embedder = embedder
        self.index    = None
        self.chunks   = []

    def build(self, chunks):
        import faiss
        texts      = [c["text"] for c in chunks]
        embeddings = self.embedder.encode(texts).astype("float32")
        dim        = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)
        self.index.add(embeddings)
        self.chunks = chunks
        print(f"[RAG] ✓ FAISS index: {self.index.ntotal} vectors (dim={dim})")

    def save(self):
        import faiss
        os.makedirs(os.path.dirname(VECTOR_STORE_PATH) or ".", exist_ok=True)
        faiss.write_index(self.index, VECTOR_STORE_PATH)
        with open(CHUNKS_STORE_PATH, "w") as f:
            json.dump(self.chunks, f)
        print(f"[RAG] ✓ Index saved -> {VECTOR_STORE_PATH}")

    def load(self):
        import faiss
        if os.path.exists(VECTOR_STORE_PATH) and os.path.exists(CHUNKS_STORE_PATH):
            self.index = faiss.read_index(VECTOR_STORE_PATH)
            with open(CHUNKS_STORE_PATH) as f:
                self.chunks = json.load(f)
            print(f"[RAG] ✓ Index loaded: {self.index.ntotal} vectors")
            return True
        return False

    def search(self, query_vec, top_k=TOP_K):
        scores, indices = self.index.search(query_vec.astype("float32"), top_k)
        return [
            (self.chunks[idx], float(score))
            for idx, score in zip(indices[0], scores[0])
            if idx != -1
        ]


# ══════════════════════════════════════════════════════════════════════════
# 4. LLM — Groq (primary) + HuggingFace (fallback)
# ══════════════════════════════════════════════════════════════════════════
def _generate_groq(messages: list) -> str | None:
    if not GROQ_API_KEY:
        return None
    try:
        resp = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {GROQ_API_KEY}",
            },
            json={
                "model": GROQ_MODEL,
                "messages": messages,
                "temperature": 0.4,
                "max_tokens": 600,
            },
            timeout=20,
        )
        if resp.status_code == 200:
            text = resp.json()["choices"][0]["message"]["content"].strip()
            print(f"[RAG] ✓ Groq response OK")
            return text
        print(f"[RAG/Groq] HTTP {resp.status_code}: {resp.text[:150]}")
    except requests.Timeout:
        print("[RAG/Groq] Timeout")
    except Exception as e:
        print(f"[RAG/Groq] Error: {e}")
    return None


def _generate_hf(prompt: str) -> str | None:
    if not HF_API_KEY:
        return None
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {HF_API_KEY}"}
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 400, "temperature": 0.4, "return_full_text": False},
    }
    try:
        resp = requests.post(
            f"https://router.huggingface.co/hf-inference/models/{HF_MODEL}",
            headers=headers, json=payload, timeout=40,
        )
        if resp.status_code == 200:
            data = resp.json()
            text = (data[0].get("generated_text","") if isinstance(data, list) else data.get("generated_text","")).strip()
            # Strip prompt artifacts
            for m in ["[/INST]","[INST]","<s>","</s>"]:
                text = text.replace(m, "")
            text = re.sub(r'\n{3,}', '\n\n', text).strip()
            if len(text) > 20:
                print("[RAG] ✓ HF response OK")
                return text
        print(f"[RAG/HF] HTTP {resp.status_code}: {resp.text[:150]}")
    except requests.Timeout:
        print("[RAG/HF] Timeout")
    except Exception as e:
        print(f"[RAG/HF] Error: {e}")
    return None


# ══════════════════════════════════════════════════════════════════════════
# 5. RAG PIPELINE
# ══════════════════════════════════════════════════════════════════════════
class RAGPipeline:
    def __init__(self):
        self.embedder = Embedder()
        self.store    = VectorStore(self.embedder)
        self._ensure_index()
        print(f"[RAG] LLM: {'Groq ✓' if GROQ_API_KEY else 'HF only'}")

    def _ensure_index(self):
        if not self.store.load():
            self._build()

    def _build(self):
        print("[RAG] Building index ...")
        from rag.knowledge_base import KNOWLEDGE_BASE
        from rag.pdf_loader import load_pdfs
        all_docs = KNOWLEDGE_BASE + load_pdfs()
        chunks = Chunker().chunk_knowledge_base(all_docs)
        self.store.build(chunks)
        self.store.save()

    def answer(self, question: str) -> dict:
        q = question.strip()

        # ── Handle greetings ──────────────────────────────────────────────
        if q.lower().rstrip("!.,?") in _GREETINGS:
            return {
                "answer": (
                    "Hello! I'm your AI medical assistant. 👋\n\n"
                    "I can help you understand medical conditions, symptoms, medications, "
                    "and test results. What medical question can I help you with today?"
                ),
                "sources": [],
            }

        # ── Semantic search ───────────────────────────────────────────────
        q_vec   = self.embedder.encode([q])
        results = self.store.search(q_vec, top_k=TOP_K)

        if not results:
            return {
                "answer": (
                    "I couldn't find relevant information on that topic in my knowledge base. "
                    "Please consult a qualified healthcare professional for personalised advice."
                ),
                "sources": [],
            }

        # ── Build sources ─────────────────────────────────────────────────
        sources, seen_titles = [], set()
        for chunk, score in results:
            title    = chunk["metadata"].get("title", "Unknown")
            category = chunk["metadata"].get("category", "")
            if title not in seen_titles:
                sources.append({
                    "title":     title,
                    "category":  category,
                    "relevance": round(score, 3),
                })
                seen_titles.add(title)
                tag = "[PDF]" if category == "pdf" else "[KB]"
                print(f"[RAG] {tag} source: '{title}' (score={score:.3f})")

        # ── Build context (top 3 chunks) ──────────────────────────────────
        context = "\n\n".join(r[0]["text"] for r in results[:3])

        # ── Try Groq first ────────────────────────────────────────────────
        answer = _generate_groq([
            {"role": "system", "content": _SYSTEM_PROMPT},
            {"role": "user",   "content": (
                f"Use the following medical knowledge to answer the question.\n\n"
                f"Medical Knowledge:\n{context}\n\n"
                f"Question: {q}"
            )},
        ])

        # ── Fallback to HuggingFace ───────────────────────────────────────
        if not answer:
            hf_prompt = (
                f"<s>[INST] {_SYSTEM_PROMPT}\n\n"
                f"Medical Knowledge:\n{context}\n\n"
                f"Question: {q} [/INST]"
            )
            answer = _generate_hf(hf_prompt)

        # ── Last resort ───────────────────────────────────────────────────
        if not answer:
            answer = (
                "I'm having trouble connecting to the AI service right now. "
                "Based on the available information, please review the sources below "
                "or consult a qualified healthcare professional."
            )

        answer += "\n\n⚕️ *This information is for educational purposes only. Always consult a qualified healthcare professional for personal medical advice.*"

        return {"answer": answer, "sources": sources}

    def rebuild_index(self):
        self._build()
        print("[RAG] ✓ Index rebuilt.")
