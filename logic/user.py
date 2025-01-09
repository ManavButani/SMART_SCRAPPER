from sqlalchemy.orm import Session
from model.user import UserInDB
from .utils import get_password_hash


def get_user(db: Session, username: str):
    return db.query(UserInDB).filter(UserInDB.username == username).first()


def create_user(
    db: Session, username: str, password: str, email: str = None, full_name: str = None
):
    hashed_password = get_password_hash(password)
    db_user = UserInDB(
        username=username,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
