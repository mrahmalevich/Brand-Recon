import requests
from app.core.config import settings
from app.core.enums import TransactionalEmailType
import logging

logger = logging.getLogger(__name__)

class LoopsEmailService:
    """Service for sending emails using loops.so."""
    
    @classmethod
    async def send_welcome_email(cls, user_email: str, first_name: str, last_name: str):
        """Send welcome email to new user."""
        try:
            response = requests.post(
                f"{settings.LOOPS_BASE_URL}/transactional",
                headers={
                    "Authorization": f"Bearer {settings.LOOPS_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "transactionalId": TransactionalEmailType.WELCOME.value,
                    "email": user_email,
                    "dataFields": {
                        "firstName": first_name,
                        "lastName": last_name
                    }
                },
                timeout=settings.DEFAULT_TIMEOUT
            )
            response.raise_for_status()
            logger.info(f"Welcome email sent to {user_email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send welcome email: {str(e)}")
            return False
    
    @classmethod
    async def send_password_reset_email(cls, user_email: str, reset_token: str, first_name: str):
        """Send password reset email."""
        try:
            reset_url = f"{settings.FRONTEND_URL}/reset-password?token={reset_token}"
            response = requests.post(
                f"{settings.LOOPS_BASE_URL}/transactional",
                headers={
                    "Authorization": f"Bearer {settings.LOOPS_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "transactionalId": TransactionalEmailType.PASSWORD_RESET.value,
                    "email": user_email,
                    "dataFields": {
                        "firstName": first_name,
                        "resetUrl": reset_url
                    }
                },
                timeout=settings.DEFAULT_TIMEOUT
            )
            response.raise_for_status()
            logger.info(f"Password reset email sent to {user_email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send password reset email: {str(e)}")
            return False 