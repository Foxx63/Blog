from sqlalchemy.orm import Session
from schemas.blog import CreateBlog
from db.models.blog import Blog

def create_new_blog(blog: CreateBlog, db: Session, author_id:int):
    # Ensure slug is generated if not provided
    slug = blog.slug or blog.title.replace(' ', '-').lower()
    
    new_blog = Blog()  # type: ignore
    new_blog.title = blog.title  # type: ignore
    new_blog.slug = slug  # type: ignore
    new_blog.content = blog.content  # type: ignore
    new_blog.image_url = blog.image_url  # type: ignore
    new_blog.author_id = author_id  # type: ignore
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def retrieve_blog(id: int, db:Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog

def list_blogs(db: Session):
    blogs = db.query(Blog).all()
    return blogs

def update_blog(id: int, blog: CreateBlog, db: Session, author_id: int = 1):
    existing_blog = db.query(Blog).filter(Blog.id == id).first()
    if not existing_blog:
        return None
    existing_blog.title = blog.title  # type: ignore
    existing_blog.slug = blog.slug  # type: ignore
    existing_blog.content = blog.content  # type: ignore
    existing_blog.image_url = blog.image_url  # type: ignore
    db.commit()
    db.refresh(existing_blog)
    return existing_blog

def delete_blog(id: int, db: Session):
    existing_blog = db.query(Blog).filter(Blog.id == id).first()
    if not existing_blog:
        return None
    db.delete(existing_blog)
    db.commit()
    return existing_blog