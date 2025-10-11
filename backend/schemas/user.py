from pydantic import BaseModel, EmailStr, Field


#properties required during user creation
class UserCreate(BaseModel):
    email : EmailStr
    # Password must be at least 4 characters long
    password : str = Field(..., min_length=4)

class ShowUser(BaseModel):
    id: int
    email : EmailStr
    is_active : bool

    class Config():  #tells pydantic to convert even non dict obj to json
        orm_mode = True