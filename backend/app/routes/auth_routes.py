from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.dependencies import get_db, authenticate_user, create_access_token, get_user
from app.dependencies import Token
from app.schemas import UserCreate, UserResponse
from app.schemas import UserBase as User
from app.utils import get_password_hash  
from app.db import collection
auth_router = APIRouter()

@auth_router.get("/signup")
async def sign():
    return {"message": "working", "status": "ok"}

@auth_router.post("/token", response_model=Token)
def login_for_access_token(db: collection = Depends(get_db),form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(
        db=db, 
        username=form_data.username, 
        password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # 3. Create the token
    access_token = create_access_token(
        data={"sub": user.username}
    )
    # 4. Return the token
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.post("/signup")
async def signup(user: UserCreate):
    print("db in /signup :", collection)
    db_user = collection.find_one({"username": user.username})
    print("db_user in /signup",db_user)
    if db_user:
       raise HTTPException(status_code=400, detail="Username already registered")
    #Hash the password 
    truncated_password = user.password[:15]
    hashed_password = get_password_hash(truncated_password)

    #Create a DICTIONARY to insert, not a "User" object
    user_document = {
        "username": user.username,
        "hashed_password": hashed_password,
        "is_active": True  # Use the default from your schema
    }

    # This expects a dict and will raise an error if you pass a Pydantic model
    result = collection.insert_one(user_document)

    # 5. Return a SAFE response.
    new_user = collection.find_one({"_id": result.inserted_id})

    # Pydantic will automatically map the fields (including _id -> id)
    # and send only the fields defined in UserResponse.
    return UserResponse(**new_user)
