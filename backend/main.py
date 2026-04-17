"""
AI Medical Hub — FastAPI Entry Point (Render-ready)
"""

import os, sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from dotenv import load_dotenv

load_dotenv()

sys.path.insert(0, os.path.dirname(__file__))

from routers.health import health_router
from routers.xray import xray_router
from routers.ocr import ocr_router
from routers.rag_chat import rag_router

app = FastAPI(
    title="AI Medical Hub",
    description="Chest X-Ray Classification | OCR Medical Report Analysis | RAG Chatbot",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api")
app.include_router(xray_router,   prefix="/api/xray")
app.include_router(ocr_router,    prefix="/api/ocr")
app.include_router(rag_router,    prefix="/api/chat")

# Serve the frontend HTML directly
FRONTEND_PATH = os.path.join(os.path.dirname(__file__), "..", "frontend", "index.html")

@app.get("/", include_in_schema=False)
async def serve_frontend():
    return FileResponse(FRONTEND_PATH)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=os.getenv("APP_HOST", "0.0.0.0"),
        # Render injects PORT; fall back to APP_PORT locally
        port=int(os.getenv("PORT", os.getenv("APP_PORT", 8000))),
        reload=False,
    )
