import requests
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class Auth0Service:
    """Service for Auth0 integration."""
    
    @classmethod
    async def register_user(cls, email: str, password: str, first_name: str, last_name: str):
        """Register a new user in Auth0."""
        try:
            token = await cls._get_management_token()
            
            response = requests.post(
                f"https://{settings.AUTH0_DOMAIN}/api/v2/users",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json"
                },
                json={
                    "email": email,
                    "password": password,
                    "connection": "Username-Password-Authentication",
                    "user_metadata": {
                        "first_name": first_name,
                        "last_name": last_name
                    }
                },
                timeout=settings.DEFAULT_TIMEOUT
            )
            response.raise_for_status()
            user_data = response.json()
            logger.info(f"User created in Auth0: {user_data['user_id']}")
            return user_data["user_id"]
        except Exception as e:
            logger.error(f"Failed to create user in Auth0: {str(e)}")
            raise
    
    @classmethod
    async def get_token(cls, username: str, password: str):
        """Get Auth0 token for a user."""
        try:
            response = requests.post(
                f"https://{settings.AUTH0_DOMAIN}/oauth/token",
                headers={"Content-Type": "application/json"},
                json={
                    "grant_type": "password",
                    "username": username,
                    "password": password,
                    "client_id": settings.AUTH0_CLIENT_ID,
                    "client_secret": settings.AUTH0_CLIENT_SECRET,
                    "audience": settings.AUTH0_API_AUDIENCE,
                    "scope": "openid profile email"
                },
                timeout=settings.DEFAULT_TIMEOUT
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Failed to get Auth0 token: {str(e)}")
            raise
    
    @classmethod
    async def exchange_code_for_token(cls, code: str):
        """Exchange authorization code for token."""
        try:
            response = requests.post(
                f"https://{settings.AUTH0_DOMAIN}/oauth/token",
                headers={"Content-Type": "application/json"},
                json={
                    "grant_type": "authorization_code",
                    "client_id": settings.AUTH0_CLIENT_ID,
                    "client_secret": settings.AUTH0_CLIENT_SECRET,
                    "code": code,
                    "redirect_uri": settings.AUTH0_CALLBACK_URL
                },
                timeout=settings.DEFAULT_TIMEOUT
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Failed to exchange code for token: {str(e)}")
            raise
    
    @classmethod
    # check how it works
    async def trigger_password_reset(cls, email: str):
        """Trigger a password reset email from Auth0."""
        try:
            response = requests.post(
                f"https://{settings.AUTH0_DOMAIN}/dbconnections/change_password",
                headers={"Content-Type": "application/json"},
                json={
                    "client_id": settings.AUTH0_CLIENT_ID,
                    "email": email,
                    "connection": "Username-Password-Authentication"
                },
                timeout=settings.DEFAULT_TIMEOUT
            )
            response.raise_for_status()
            logger.info(f"Password reset triggered for {email}")
            return True
        except Exception as e:
            logger.error(f"Failed to trigger password reset: {str(e)}")
            return False
    
    @classmethod
    async def _get_management_token(cls):
        """Get Auth0 management API token."""
        try:
            response = requests.post(
                f"https://{settings.AUTH0_DOMAIN}/oauth/token",
                headers={"Content-Type": "application/json"},
                json={
                    "grant_type": "client_credentials",
                    "client_id": settings.AUTH0_CLIENT_ID,
                    "client_secret": settings.AUTH0_CLIENT_SECRET,
                    "audience": f"https://{settings.AUTH0_DOMAIN}/api/v2/"
                },
                timeout=settings.DEFAULT_TIMEOUT
            )
            response.raise_for_status()
            return response.json()["access_token"]
        except Exception as e:
            logger.error(f"Failed to get management token: {str(e)}")
            raise 