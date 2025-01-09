from fastapi import APIRouter, HTTPException, Depends
from schema.user import User, UserCreate
from core.database import get_db
from logic.user import create_user, get_user
from logic.auth import get_current_active_user
from sqlalchemy.orm import Session

router = APIRouter()


# User creation route
@router.post("/register/", response_model=User)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, user.username)  # Check if the user already exists
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(
        db,
        username=user.username,
        password=user.password,
    )


@router.get("/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
