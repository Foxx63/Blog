from sqlalchemy.orm import Session

from schemas.user import UserCreate
from db.models.user import User
from core.security import get_password_hash


def create_new_user(user:UserCreate,db:Session):
    new_user = User(
        email = user.email,
        password=get_password_hash(user.password),  # Hash the password
        is_active=True,
        is_superuser=False
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def retrieve_user(id: int, db:Session):
    user = db.query(User).filter(User.id == id).first()
    return user

def list_users(db:Session):
    users = db.query(User).all()
    return users

def get_user_by_email(email: str, db:Session):
    user = db.query(User).filter(User.email == email).first()
    return user