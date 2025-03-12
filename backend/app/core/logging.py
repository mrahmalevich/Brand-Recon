import logging
import sys
from logging.handlers import RotatingFileHandler
from app.core.config import settings

def setup_logging():
    """Configure logging for the application."""

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(detailed_formatter)
    root_logger.addHandler(console_handler)
    
    if settings.LOG_FILE:
        file_handler = RotatingFileHandler(
            settings.LOG_FILE,
            maxBytes=10485760,  # 10MB
            backupCount=5
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(detailed_formatter)
        root_logger.addHandler(file_handler)
    
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("fastapi").setLevel(logging.WARNING)
    
    return root_logger 