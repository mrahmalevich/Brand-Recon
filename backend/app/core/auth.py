from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from jose import jwt
import requests
from app.core.config import settings

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"https://{settings.AUTH0_DOMAIN}/authorize",
    tokenUrl=f"https://{settings.AUTH0_DOMAIN}/oauth/token",
)

async def get_token_payload(token: str = Depends(oauth2_scheme)):
    try:
        jwks_url = f"https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json"
        jwks = requests.get(jwks_url, timeout=settings.DEFAULT_TIMEOUT).json()
        
        payload = jwt.decode(
            token,
            jwks,
            algorithms=["RS256"],
            audience=settings.AUTH0_API_AUDIENCE,
            issuer=f"https://{settings.AUTH0_DOMAIN}/"
        )
        return payload
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        ) from e

def get_token_payload_dependency():
    return get_token_payload

async def get_current_user():
    """Get the current user from the token payload."""
    payload = await get_token_payload()
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user ID in token",
        )
    return user_id 