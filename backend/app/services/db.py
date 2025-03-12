from app.core.database import get_database
from app.models.user import User
import logging

logger = logging.getLogger(__name__)

class DatabaseService:
    """Service for database operations."""

    def __init__(self):
        self.db = None

    async def _get_db(self):
        """Get database connection lazily."""
        if self.db is None:
            self.db = await get_database()
        return self.db

    async def find_user_by_email(self, email: str):
        """Find a user by email."""
        try:
            db = await self._get_db()
            query = {"email": email}
            user_data = await db["users"].find_one(query)
            if not user_data:
                return None
            return User.from_mongo(user_data)
        except Exception as e:
            logger.error(f"Error finding user by email: {str(e)}")
            raise

    async def find_user_by_id(self, user_id):
        """Find a user by ID."""
        try:
            db = await self._get_db()
            query = {"_id": user_id}
            user_data = await db["users"].find_one(query)
            if not user_data:
                return None
            return User.from_mongo(user_data)
        except Exception as e:
            logger.error(f"Error finding user by ID: {str(e)}")
            raise

    async def find_user_by_reset_token(self, token: str, expiry_time):
        """Find a user by password reset token."""
        try:
            db = await self._get_db()
            query = {
                "password_reset_token": token,
                "password_reset_expires": {"$gt": expiry_time}
            }
            user_data = await db["users"].find_one(query)
            if not user_data:
                return None
            return User.from_mongo(user_data)
        except Exception as e:
            logger.error(f"Error finding user by reset token: {str(e)}")
            raise

    async def create_user(self, user: User):
        """Create a new user."""
        try:
            db = await self._get_db()
            result = await db["users"].insert_one(user.to_mongo())
            user.id = result.inserted_id
            return user
        except Exception as e:
            logger.error(f"Error creating user: {str(e)}")
            raise

    async def update_user_last_login(self, user_id, last_login_time):
        """Update user's last login time."""
        try:
            db = await self._get_db()
            query = {"_id": user_id}
            update = {"$set": {"last_login": last_login_time}}
            await db["users"].update_one(query, update)
        except Exception as e:
            logger.error(f"Error updating user last login: {str(e)}")
            raise

    async def update_user_reset_token(self, user_id, token, expires):
        """Update user's password reset token."""
        try:
            db = await self._get_db()
            query = {"_id": user_id}
            update = {"$set": {
                "password_reset_token": token,
                "password_reset_expires": expires
            }}
            await db["users"].update_one(query, update)
        except Exception as e:
            logger.error(f"Error updating user reset token: {str(e)}")
            raise

    async def update_user_password(self, user_id, hashed_password):
        """Update user's password."""
        try:
            db = await self._get_db()
            query = {"_id": user_id}
            update = {"$set": {
                "hashed_password": hashed_password,
                "password_reset_token": None,
                "password_reset_expires": None
            }}
            await db["users"].update_one(query, update)
        except Exception as e:
            logger.error(f"Error updating user password: {str(e)}")
            raise 