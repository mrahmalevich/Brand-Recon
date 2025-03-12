from app.models.user import User
from app.utils.security import get_password_hash, verify_password, generate_password_reset_token, get_password_reset_expiry
from fastapi import HTTPException, status
from app.services.db import DatabaseService
from app.services.auth0 import Auth0Service
from app.services.email import LoopsEmailService
import logging

logger = logging.getLogger(__name__)

class UserService:
    """Service for user management."""

    def __init__(self):
        self.db_service = DatabaseService()
        self.auth0_service = Auth0Service()
        self.email_service = LoopsEmailService()

    async def register_user(self, email: str, password: str, first_name: str, last_name: str, organization: str):
        """Register a new user."""

        try:
            try:
                existing_user = await self.db_service.find_user_by_email(email)
            except Exception as e:
                logger.error(f"Failed to find user by email: {str(e)}")
                raise

            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User with this email already exists"
                )

            try:
                auth0_id = await self.auth0_service.register_user(
                    email,
                    password,
                    first_name,
                    last_name
                )
            except Exception as e:
                logger.error(f"Failed to register user in Auth0: {str(e)}")
                raise

            user = User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                organization=organization,
                hashed_password=get_password_hash(password),
                auth0_id=auth0_id
            )

            try:
                user = await self.db_service.create_user(user)
            except Exception as e:
                logger.error(f"Failed to create user in database: {str(e)}")
                raise

            try:
                await self.email_service.send_welcome_email(email, first_name, last_name)
            except Exception as e:
                logger.error(f"Failed to send welcome email: {str(e)}")

            return user
        except Exception as e:
            logger.error(f"Failed to register user: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to register user"
            ) from e

    async def authenticate_user(self, email: str, password: str):
        """Authenticate a user."""

        try:
            try:
                user = await self.db_service.find_user_by_email(email)
            except Exception as e:
                logger.error(f"Failed to find user by email: {str(e)}")
                raise
        
            if not user:
                return False

            if not verify_password(password, user.hashed_password):
                return False

            try:
                await self.db_service.update_user_last_login(user.id, get_password_reset_expiry())
            except Exception as e:
                logger.error(f"Failed to update user last login: {str(e)}")

            return user
        except Exception as e:
            logger.error(f"Failed to authenticate user: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to authenticate user"
            ) from e

    async def login(self, email: str, password: str):
        """Authenticate user and get auth token in one step."""

        try:
            try:
                user = await self.authenticate_user(email, password)
            except Exception as e:
                logger.error(f"Failed to authenticate user: {str(e)}")
                raise

            if not user:
                return None

            try:
                token_data = await self.auth0_service.get_token(email, password)
            except Exception as e:
                logger.error(f"Failed to get token: {str(e)}")
                raise

            return {
                "user": user,
                "token_data": token_data
            }
        except Exception as e:
            logger.error(f"Failed to get token for user {email}: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to get token for user {email}: {str(e)}"
            ) from e

    async def request_password_reset(self, email: str):
        """Request a password reset."""

        try:
            try:
                user = await self.db_service.find_user_by_email(email)
            except Exception as e:
                logger.error(f"Failed to find user by email: {str(e)}")
                raise

            if not user:
                return True

            token = generate_password_reset_token()
            expires = get_password_reset_expiry()

            try:
                await self.db_service.update_user_reset_token(user.id, token, expires)
            except Exception as e:
                logger.error(f"Failed to update user reset token: {str(e)}")
                raise

            try:
                await self.email_service.send_password_reset_email(email, token, user.first_name)
            except Exception as e:
                logger.error(f"Failed to send password reset email: {str(e)}")
                raise

            return True
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to find user by email"
            ) from e

    async def reset_password(self, token: str, new_password: str):
        """Reset a user's password."""
        try:
            user = await self.db_service.find_user_by_reset_token(
                token,
                get_password_reset_expiry()
            )

            if not user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid or expired token"
                )

            hashed_password = get_password_hash(new_password)
            await self.db_service.update_user_password(
                user.id,
                hashed_password
            )

            return True
        except Exception as e:
            logger.error(f"Failed to reset password: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to reset password"
            ) from e
        
    async def get_user_by_email(self, email: str):
        """Get a user by email."""
        return await self.db_service.find_user_by_email(email)

    async def get_user_by_id(self, user_id: str):
        """Get a user by ID."""
        return await self.db_service.find_user_by_id(user_id)
