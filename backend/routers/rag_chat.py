"""
RAG Chat Router — Fixed
"""

import os, sys
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv

load_dotenv()
rag_router = APIRouter()

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

_pipeline = None


def _get_pipeline():
    global _pipeline
    if _pipeline is None:
        backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        os.chdir(backend_dir)
        sys.path.insert(0, backend_dir)
        from rag.rag_engine import RAGPipeline
        _pipeline = RAGPipeline()
    return _pipeline


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000)


class SourceRef(BaseModel):
    title:     str
    category:  str
    relevance: float


class ChatResponse(BaseModel):
    answer:  str
    sources: List[SourceRef]


@rag_router.post("/ask", response_model=ChatResponse)
async def ask_question(body: ChatRequest):
    try:
        pipeline = _get_pipeline()
    except Exception as e:
        raise HTTPException(503, f"RAG pipeline failed to load: {e}")

    try:
        result = pipeline.answer(body.question)
    except Exception as e:
        raise HTTPException(500, f"Error generating answer: {e}")

    return ChatResponse(
        answer=result["answer"],
        sources=[SourceRef(**s) for s in result.get("sources", [])],
    )


@rag_router.get("/rebuild-index")
async def rebuild_index():
    try:
        pipeline = _get_pipeline()
        pipeline.rebuild_index()
        return {"status": "ok", "message": "Index rebuilt successfully."}
    except Exception as e:
        raise HTTPException(500, str(e))
