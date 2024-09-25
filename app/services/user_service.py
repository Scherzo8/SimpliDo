from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hashed



def create_user(db: Session, user: UserCreate) -> User:
    """
    Create a new user in the database
    
    Args:
        db (Session): SQLAlchemy session for database interaction.
        user (UserCreate): The user data to be created.
        
    Returns:
        User: The created user object.
    """

    db_user = User(username=user.username, 
                   email=user.email, 
                   hashed_password=get_password_hashed(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_username(db:Session, username:str) -> User | None:
    """
    Retrieves a user by username.
    
    Args:
        db (Session): SQLAlchemy session for database interaction.
        username (str): The username of user.
    
    Returns:
        User | None: The user object is found or None
    """

    return db.query(User).filter(User.username == username).first()
