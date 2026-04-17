from fastapi import APIRouter
from pydantic import BaseModel

health_router = APIRouter()

class HealthResponse(BaseModel):
    status: str
    message: str

@health_router.get("/health", response_model=HealthResponse)
async def health():
    return {"status": "ok", "message": "AI Medical Hub backend is running."}
