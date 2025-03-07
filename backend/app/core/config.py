from typing import List, Any
import json
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Brand Recon API"
    API_V1_STR: str = "/api/v1"
    
    ENVIRONMENT: str = "development"
    
    MONGODB_URL: str = ""
    MONGODB_DB_NAME: str = "brand_recon"
        
    SECRET_KEY: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    BACKEND_CORS_ORIGINS: List[str] = []
    
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