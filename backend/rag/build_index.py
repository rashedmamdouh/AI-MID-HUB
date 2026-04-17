#!/usr/bin/env python
"""
build_index.py — Builds the FAISS vector index from:
  1. The built-in knowledge base (knowledge_base.py)
  2. Any PDF files placed in:  backend/rag/pdfs/

Usage:
    cd backend
    python rag/build_index.py

Re-run every time you add or remove PDFs from rag/pdfs/.
"""
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
os.chdir(os.path.join(os.path.dirname(__file__), ".."))

from rag.rag_engine import RAGPipeline

if __name__ == "__main__":
    print("=" * 55)
    print("  AI Medical Hub — Building RAG Vector Index")
    print("=" * 55)
    print("  Drop PDFs into:  backend/rag/pdfs/")
    print("  Then re-run this script to include them.")
    print("=" * 55)
    pipeline = RAGPipeline()
    pipeline.rebuild_index()
    print("\n✓ Done. Index is ready. Start the server now.")
