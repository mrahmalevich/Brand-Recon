from typing import List, Any
import json
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Brand Recon API"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    FRONTEND_URL: str = ""
    BACKEND_CORS_ORIGINS: List[str] = []
    SECRET_KEY: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    DEFAULT_TIMEOUT: int = 10

    # Logging settings
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = ""  # Empty means log to console only

    MONGODB_URL: str = ""
    MONGODB_DB_NAME: str = "brand_recon"

    AUTH0_DOMAIN: str = ""
    AUTH0_CLIENT_ID: str = ""
    AUTH0_CLIENT_SECRET: str = ""
    AUTH0_API_AUDIENCE: str = ""
    AUTH0_CALLBACK_URL: str = ""

    LOOPS_BASE_URL: str = "https://app.loops.so/api/v1"
    LOOPS_API_KEY: str = ""
    
    class Config:
        env_file = [".env.local", ".env"]
        env_file_encoding = "utf-8"
        
        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str) -> Any:
            if field_name == "BACKEND_CORS_ORIGINS":
                try:
                    return json.loads(raw_val)
                except (json.JSONDecodeError, TypeError):
                    return []
            return raw_val

settings = Settings() 