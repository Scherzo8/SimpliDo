import os
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.models.user import User
from app.database.db import get_db



SECRET_KEY = os.getenv("SECRET_KEY", "Test123")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")

pwd_context = CryptContext(schemas=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_password_hashed(password: str) -> str:
    """
    Hash password using bcrypt.
    
    Args:
        password (str): The password to hashed.
    
    Returns:   
        str: The hashed password.
    """

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.
    
    Args:
        plain_password (str): The plain password to verify.
        hashed_password (str): The hashed password.
        
    Returns:
        bool: True if password match, False otherwise.
    """

    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Create a JWT access token.
    
    Args:
        data (dict): The payload for the token'
        expires_delta (timedelta | None): Optional expiration time.
    
     Returns:
        str: The generated access token.
    """

    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    """
    Retrieve the current user from the token
    
    Args:
        token (str): The JWT token.
        db (Session): SQLAlchemy session for database interaction.
        
    Returns:
        User: The current user object.
    
    Raises:
        HTTPException: if the token is invalid or the user does not exist.
    """

    credentials_exception = HTTPException(status_code=401,
                                          details="Could not validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if not username:
            raise credentials_exception
    
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise credentials_exception
    
    return user

