from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from .base import BaseResponse

class UserCreateRequest(BaseModel):
    """Schema for user creation request."""
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: Optional[str] = None
    password: str = Field(..., min_length=8)

class UserUpdateRequest(BaseModel):
    """Schema for user update request."""
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    full_name: Optional[str] = None
    password: Optional[str] = Field(None, min_length=8)

class UserSchema(BaseModel):
    """Base user schema for responses."""
    id: str
    email: EmailStr
    username: str
    full_name: Optional[str] = None
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

class UserResponse(BaseResponse):
    """Schema for user response."""
    user: UserSchema

class UsersListResponse(BaseResponse):
    """Schema for users list response."""
    users: list[UserSchema] 