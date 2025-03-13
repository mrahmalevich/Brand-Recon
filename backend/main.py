from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.config import settings
from app.core.database import connect_to_mongo, close_mongo_connection
from app.api.v1.api import api_router
from app.core.logging import setup_logging

logger = setup_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: place startup code here
    logger.info("Starting up application")
    await connect_to_mongo()
    logger.info("Connected to MongoDB")
    yield
    # Shutdown: place shutdown code here
    logger.info("Shutting down application")
    await close_mongo_connection()
    logger.info("Disconnected from MongoDB")

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info(f"API will be available at {settings.API_V1_STR}")
app.include_router(api_router, prefix=settings.API_V1_STR)