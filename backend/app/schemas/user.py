from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from .base import BaseResponse

# Request Schemas
class UserRegisterRequest(BaseModel):
    """Schema for user registration request."""
    email: EmailStr
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    organization: str = Field(..., min_length=1, max_length=100)
    password: str = Field(..., min_length=8)

class UserLoginRequest(BaseModel):
    """Schema for user login request."""
    email: EmailStr
    password: str

class PasswordResetRequest(BaseModel):
    """Schema for password reset request."""
    email: EmailStr

class PasswordResetConfirmRequest(BaseModel):
    """Schema for password reset confirmation."""
    token: str
    password: str = Field(..., min_length=8)

class UserUpdateRequest(BaseModel):
    """Schema for user update request."""
    first_name: Optional[str] = Field(None, min_length=1, max_length=50)
    last_name: Optional[str] = Field(None, min_length=1, max_length=50)
    organization: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None

# Response Schemas
class UserSchema(BaseModel):
    """Base user schema for responses."""
    id: str
    email: EmailStr
    first_name: str
    last_name: str
    organization: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    
class UserResponse(BaseResponse):
    """Schema for user response."""
    user: UserSchema

class TokenResponse(BaseResponse):
    """Schema for token response."""
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    id_token: Optional[str] = None

class UsersListResponse(BaseResponse):
    """Schema for users list response."""
    users: list[UserSchema] 