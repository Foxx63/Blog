from typing import Optional
from pydantic import BaseModel, root_validator
from datetime import date



class CreateBlog(BaseModel):
    title: str
    image_url: Optional[str] = None
    content: Optional[str] = None
    slug: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if 'title' in values and not values.get('slug'):
            values['slug'] = values.get('title').replace(' ', '-').lower()
   
        return values

class UpdateBlog(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None   

class ShowBlog(BaseModel):
    id: int
    title:str 
    content: Optional[str]
    image_url: Optional[str]
    author_id: int
    created_at: date

    class Config:
        orm_mode = True