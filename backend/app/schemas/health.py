from pydantic import BaseModel

class HealthStatus(BaseModel):
    """Health status information."""
    success: bool
    message: str
    status: str
    version: str
    environment: str