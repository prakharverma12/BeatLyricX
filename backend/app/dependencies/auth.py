from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.utils import verify_password, get_password_hash, create_access_token
from .token import TokenData
from app.db import collection
from app.schemas import UserInDB, UserResponse

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")
def get_db():
    db = collection
    try:
        yield db
    finally:
        pass

def get_user(db: collection, username: str):
    """
    Fetches a user from the MongoDB collection by username.
    """
    # Use PyMongo's .find_one() method
    # It expects a dictionary as the query filter
    user_data = db.find_one({"username": username})
    
    if user_data:
        # Convert the dictionary from MongoDB into your Pydantic User model
        return UserResponse(**user_data)
        
    return None # Return None if user not found

def authenticate_user(db, username: str, password: str):
    user_data = db.find_one({"username": username})
    if not user_data:
        return None # User not found
    print("auth user fxn user_data: ",user_data)
    # 2. Parse user data
    user = UserInDB(**user_data)
    print("auth user fxn user variable: ",user)
    # 3. Truncate incoming password *exactly* as you do at signup
    password_to_check = password[:15]

    # 4. Use the correct VERIFY function
    if not verify_password(password_to_check, user.hashed_password):
        return None # Invalid password

    return user # Authentication successful

def get_current_user(db= collection, token: str = Depends(oauth2_scheme)):
    
    return user