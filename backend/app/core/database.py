from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class Database:
    client: AsyncIOMotorClient = None
    
db = Database()

async def connect_to_mongo():
    """Connect to MongoDB."""
    logger.info("Connecting to MongoDB...")
    db.client = AsyncIOMotorClient(settings.MONGODB_URL)
    logger.info("Connected to MongoDB")

async def close_mongo_connection():
    """Close MongoDB connection."""
    logger.info("Closing MongoDB connection...")
    if db.client:
        db.client.close()
    logger.info("MongoDB connection closed")

async def get_database():
    """Get database connection."""
    return db.client[settings.MONGODB_DB_NAME] 