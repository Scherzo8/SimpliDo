from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserOut
from services.user_service import create_user, get_user_by_username
from core.security import verify_password, create_access_token
from database.db import get_db

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)) -> UserOut:
    """
    API endpoint to register a new user
    
    Args:
        user (UserCreate): The user data for registration
        db (Session): SQLAlchemy session for database interaction
    
    Returns:
        UserOut: The created user data
    """

    db_user = get_user_by_username(db, user.username)

    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    return create_user(db, user)

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)) -> dict:
    """
    API endpoint for user login.
    
    Args:
        username (str): the user's username.
        password (str): The user's password.
        db (Session): SQLAlchemy session for database interaction
    
    Returns:
        dict: Access token for user.
    """

    user = get_user_by_username(db, username)

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    access_token = create_access_token(data={"sub": user.username})

    return {"access token": access_token, "token_type": "bearer"}