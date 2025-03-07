from app.models.user import User
from app.schemas.user import UserSchema, UserCreateRequest

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

def user_create_request_to_model(user_create: UserCreateRequest, hashed_password: str) -> User:
    """Convert UserCreateRequest to User model."""
    return User(
        email=user_create.email,
        username=user_create.username,
        full_name=user_create.full_name,
        hashed_password=hashed_password,
        is_active=True,
        is_superuser=False
    ) 