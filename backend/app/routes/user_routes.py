
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_current_user, get_db
from app.schemas import UserResponse, UserInDB

user_router = APIRouter()

@user_router.get("/me", response_model=UserResponse)
def read_users_me(current_user: UserInDB = Depends(get_current_user)):
    return current_user