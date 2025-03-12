from app.models.user import User
from app.schemas.user import UserSchema

def user_model_to_schema(user: User) -> UserSchema:
    """Convert User model to UserSchema."""
    return UserSchema(
        id=str(user.id),
        email=user.email,
        username=user.username,
        full_name=user.full_name,
        is_active=user.is_active,
        is_superuser=user.is_superuser,
        created_at=user.created_at,
        updated_at=user.updated_at
    )