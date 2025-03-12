from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserRegisterRequest, UserLoginRequest, UserResponse, TokenResponse, PasswordResetRequest, PasswordResetConfirmRequest
from app.services.user import UserService
from app.utils.model_converters import user_model_to_schema

router = APIRouter()
user_service = UserService()

@router.post("/register", response_model=UserResponse)
async def register(user_data: UserRegisterRequest):
    """
    Register a new user.
    """
    try:
        user = await user_service.register_user(
            email=user_data.email,
            password=user_data.password,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            organization=user_data.organization
        )
        return {
            "success": True,
            "message": "User registered successfully",
            "user": user_model_to_schema(user)
        }
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while registering user"
        ) from e

@router.post("/login", response_model=TokenResponse)
async def login(login_data: UserLoginRequest):
    """
    Authenticate a user and return a token.
    """
    try:
        login_result = await user_service.login(login_data.email, login_data.password)
        if not login_result:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        token_data = login_result["token_data"]
        return {
            "success": True,
            "message": "Login successful",
            "access_token": token_data["access_token"],
            "token_type": token_data["token_type"],
            "expires_in": token_data["expires_in"],
            "id_token": token_data.get("id_token")
        }
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during login"
        ) from e

@router.post("/password-reset/request", response_model=UserResponse)
async def request_password_reset(reset_data: PasswordResetRequest):
    """
    Request a password reset.
    """
    try:
        await user_service.request_password_reset(reset_data.email)
        return {
            "success": True,
            "message": "If your email is registered, you will receive a password reset link"
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while requesting password reset"
        ) from e

@router.post("/password-reset/confirm", response_model=UserResponse)
async def confirm_password_reset(reset_data: PasswordResetConfirmRequest):
    """
    Confirm a password reset.
    """
    try:
        await user_service.reset_password(reset_data.token, reset_data.password)
        return {
            "success": True,
            "message": "Password has been reset successfully"
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired token"
        ) from e

# @router.get("/callback", response_model=TokenResponse)
# async def auth_callback(code: str):
#     """
#     Handle Auth0 callback.
#     """
#     try:
#         response = await auth0_service.exchange_code_for_token(code)
#         return {
#             "success": True,
#             "message": "Authentication successful",
#             "access_token": response["access_token"],
#             "token_type": response["token_type"],
#             "expires_in": response["expires_in"],
#             "id_token": response.get("id_token")
#         }
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"Failed to authenticate: {str(e)}"
#         ) from e