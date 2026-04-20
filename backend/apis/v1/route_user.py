from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from schemas.user import UserCreate, ShowUser
from db.session import get_db
from db.repository.user import create_new_user, retrieve_user, list_users

router = APIRouter()


@router.post("/", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_new_user(user=user, db=db)
    return new_user

@router.get("/users", response_model=List[ShowUser])
def get_all_users(db: Session = Depends(get_db)):
    users = list_users(db=db)
    return users

@router.get("/user/{id}", response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user = retrieve_user(id=id, db=db)
    if not user:
        raise HTTPException(detail=f"User with ID {id} does not exist.", status_code=status.HTTP_404_NOT_FOUND)
    return user