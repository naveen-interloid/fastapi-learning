from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    bookname : str
    user_id : int
    
class BookCreate(BookBase):
   pass

class BookResponse(BookBase):
    id : int
    
    model_config = ConfigDict(from_attributes=True)
    
class BookInUserResponse(BaseModel):
    id : int
    bookname : str