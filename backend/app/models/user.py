from .base import DBModelBase

class User(DBModelBase):
    """User database model."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.email = kwargs.get("email")
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.organization = kwargs.get("organization")
        self.hashed_password = kwargs.get("hashed_password")
        self.is_active = kwargs.get("is_active", True)
        self.is_verified = kwargs.get("is_verified", False)
        self.auth0_id = kwargs.get("auth0_id")
        self.last_login = kwargs.get("last_login")
        self.password_reset_token = kwargs.get("password_reset_token")
        self.password_reset_expires = kwargs.get("password_reset_expires")
    
    def to_mongo(self):
        """Convert model instance to MongoDB document."""
        data = super().to_mongo()
        data.update({
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "organization": self.organization,
            "hashed_password": self.hashed_password,
            "is_active": self.is_active,
            "is_verified": self.is_verified,
            "auth0_id": self.auth0_id,
            "last_login": self.last_login,
            "password_reset_token": self.password_reset_token,
            "password_reset_expires": self.password_reset_expires
        })
        return data 