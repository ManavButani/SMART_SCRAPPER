# models.py

from sqlalchemy import Column, Integer, String, Boolean
from core.database import Base


class UserInDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, index=True, nullable=True)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)
