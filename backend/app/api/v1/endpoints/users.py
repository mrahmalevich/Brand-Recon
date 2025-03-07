from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.core.database import get_database
from app.models.user import User
from app.utils.security import get_password_hash
from app.schemas.user import UserCreateRequest, UserResponse
router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user(user_in: UserCreateRequest, db=Depends(get_database)):
    if await db["users"].find_one({"email": user_in.email}):
        raise HTTPException(
            status_code=400,
            detail="User with this email already exists"
        )
    
    user = User(
        **user_in.model_dump(exclude={"password"}),
        hashed_password=get_password_hash(user_in.password)
    )
    
    result = await db["users"].insert_one(user.to_mongo())
    user.id = result.inserted_id
    return user

@router.get("/", response_model=List[UserResponse])
async def get_users(skip: int = 0, limit: int = 10, db=Depends(get_database)):
    users = await db["users"].find().skip(skip).limit(limit).to_list(length=limit)
    return users 