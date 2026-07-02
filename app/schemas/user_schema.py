from pydantic import BaseModel, ConfigDict

from app.schemas.book_schema import BookInUserResponse


class UserBase(BaseModel):
    username : str
    email : str
    
class UserCreate(UserBase):
    password:str


class UserResponse(UserBase):
    id : int
    books:list[BookInUserResponse]
    
    model_config = ConfigDict(from_attributes=True)
    
class UserUpdate(UserBase):
    pass

