from datetime import datetime
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class DBModelBase:
    """Base class for database models."""
    def __init__(self, **kwargs):
        self.id = kwargs.get("_id", None)
        self.created_at = kwargs.get("created_at", datetime.utcnow())
        self.updated_at = kwargs.get("updated_at", datetime.utcnow())
    
    @classmethod
    def from_mongo(cls, data):
        """Convert MongoDB document to model instance."""
        if not data:
            return None
        return cls(**data)
    
    def to_mongo(self):
        """Convert model instance to MongoDB document."""
        return {
            "_id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        } 