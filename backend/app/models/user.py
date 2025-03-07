from .base import DBModelBase

class User(DBModelBase):
    """User database model."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.email = kwargs.get("email")
        self.username = kwargs.get("username")
        self.full_name = kwargs.get("full_name")
        self.hashed_password = kwargs.get("hashed_password")
        self.is_active = kwargs.get("is_active", True)
        self.is_superuser = kwargs.get("is_superuser", False)
    
    def to_mongo(self):
        """Convert model instance to MongoDB document."""
        data = super().to_mongo()
        data.update({
            "email": self.email,
            "username": self.username,
            "full_name": self.full_name,
            "hashed_password": self.hashed_password,
            "is_active": self.is_active,
            "is_superuser": self.is_superuser
        })
        return data 