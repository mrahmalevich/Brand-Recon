from pydantic import BaseModel
from .base import BaseResponse


class HealthStatus(BaseModel):
    """Health status information."""
    success: bool
    message: str
    status: str
    version: str
    environment: str