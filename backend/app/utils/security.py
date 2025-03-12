from passlib.context import CryptContext
import secrets
from datetime import datetime, timedelta

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hash."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Generate a password hash."""
    return pwd_context.hash(password)

# Token generation for password reset
def generate_password_reset_token() -> str:
    """Generate a secure token for password reset."""
    return secrets.token_urlsafe(32)

def get_password_reset_expiry() -> datetime:
    """Get the expiry time for a password reset token."""
    return datetime.now(datetime.UTC) + timedelta(hours=24)