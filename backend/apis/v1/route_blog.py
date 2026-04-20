from fastapi import HTTPException, APIRouter, status
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from db.session import get_db
from schemas.blog import ShowBlog, CreateBlog
from db.repository.blog import create_new_blog, retrieve_blog, list_blogs, update_blog, delete_blog
from apis.v1.route_auth import get_current_user 
from db.models.user import User
router = APIRouter()

@router.post("/blogs", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
async def create_blog(blog: CreateBlog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_blog = create_new_blog(blog=blog, db=db, author_id=current_user.id)
    return new_blog

@router.get("/blog/{id}", response_model=ShowBlog)
async def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        raise HTTPException(detail=f"Blog with ID {id} does not exist.", status_code=status.HTTP_404_NOT_FOUND)
    return blog

@router.get("/blogs", response_model=List[ShowBlog])
async def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs

@router.put("/blog/{id}", response_model=ShowBlog)
async def update_blog_route(id: int, blog: CreateBlog, db: Session = Depends(get_db)):
    updated_blog = update_blog(id=id, blog=blog, db=db, author_id=1)
    if not updated_blog:
        raise HTTPException(detail=f"Blog with ID {id} does not exist.", status_code=status.HTTP_404_NOT_FOUND)
    return updated_blog

@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog_route(id: int, db: Session = Depends(get_db)):
    deleted_blog = delete_blog(id=id, db=db)
    if not deleted_blog:
        raise HTTPException(detail=f"Blog with ID {id} does not exist.", status_code=status.HTTP_404_NOT_FOUND)
    return None