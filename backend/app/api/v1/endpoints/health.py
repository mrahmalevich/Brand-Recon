from fastapi import APIRouter
from app.schemas.health import HealthStatus
from app.core.config import settings

router = APIRouter()

@router.get("/", response_model=HealthStatus)
async def health_check():
    """
    Health check endpoint to verify API is running.
    Returns basic information about the API status.
    """
    return {
        "success": True,
        "message": "API is running",
        "status": "healthy",
        "version": "1.0.0",
        "environment": settings.ENVIRONMENT
    } 