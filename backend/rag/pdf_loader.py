"""
pdf_loader.py — Load all PDFs from rag/pdfs/ into knowledge-base format.

Drop any medical PDF into:  backend/rag/pdfs/
Then rebuild the index:     cd backend && python rag/build_index.py
"""

import os, re

PDF_DIR = os.path.join(os.path.dirname(__file__), "pdfs")


def _extract_text_pypdf(path: str) -> str:
    from pypdf import PdfReader
    reader = PdfReader(path)
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text.strip())
    return "\n\n".join(pages)


def _clean(text: str) -> str:
    # Normalise whitespace
    text = re.sub(r'[ \t]{3,}', '  ', text)
    text = re.sub(r'\n{4,}', '\n\n', text)
    # Drop lines that are just page numbers or single characters
    lines = [l for l in text.splitlines() if len(l.strip()) > 3]
    return "\n".join(lines).strip()


def load_pdfs() -> list:
    """
    Returns a list of knowledge-base dicts:
        [{"title": str, "category": str, "text": str}, ...]
    One entry per PDF file.
    """
    if not os.path.isdir(PDF_DIR):
        return []

    docs = []
    pdf_files = [f for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("[PDF] No PDFs found in rag/pdfs/")
        return []

    for filename in sorted(pdf_files):
        path = os.path.join(PDF_DIR, filename)
        title = os.path.splitext(filename)[0].replace("_", " ").replace("-", " ").title()
        try:
            raw = _extract_text_pypdf(path)
            text = _clean(raw)
            if len(text) < 50:
                print(f"[PDF] WARNING: '{filename}' yielded very little text — skipping.")
                continue
            docs.append({
                "title":    title,
                "category": "pdf",
                "text":     text,
            })
            print(f"[PDF] ✓ Loaded '{filename}' ({len(text):,} chars)")
        except Exception as e:
            print(f"[PDF] ERROR loading '{filename}': {e}")

    print(f"[PDF] {len(docs)} PDF(s) loaded.")
    return docs
