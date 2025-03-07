from fastapi import APIRouter
from .endpoints import health
from .endpoints import users

api_router = APIRouter()
api_router.include_router(health.router, prefix="/api/v1/health", tags=["health"]) 
api_router.include_router(users.router, prefix="/api/v1/users", tags=["users"]) 