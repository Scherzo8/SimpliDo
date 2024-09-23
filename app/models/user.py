from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.db import Base



class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)

    tasks = relationship("Tasks", back_populates="owner")