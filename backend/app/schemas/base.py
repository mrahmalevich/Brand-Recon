from pydantic import BaseModel
from typing import Optional, Any, Dict, List

class BaseResponse(BaseModel):
    """Base response model with success status and message."""
    success: bool = True
    message: str = "Operation successful"

class ErrorResponse(BaseResponse):
    """Error response model."""
    success: bool = False
    message: str = "An error occurred"
    error_details: Optional[Dict[str, Any]] = None

class PaginatedResponse(BaseModel):
    """Base model for paginated responses."""
    total: int
    page: int
    page_size: int
    pages: int
    items: List[Any] 