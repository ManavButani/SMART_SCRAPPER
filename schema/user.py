from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    password: str


class User(BaseModel):
    id: int
    username: str
    disabled: Optional[bool] = None

    class Config:
        from_attributes = True
