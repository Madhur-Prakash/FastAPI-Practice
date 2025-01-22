from typing import List, Optional
from pydantic import BaseModel

#pydantic model are schemas and sql alchemy models are models

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
         form_attributes = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs : List[Blog] =[]
    class Config():
         form_attributes = True

class ShowBlog(BaseModel):
    title: str
    body:str
    creator: ShowUser

    class Config():
          # orm_mode = True # --> was used in the previous version of pydanctic
        
        form_attributes = True # used in V2 of pydantic --> Use Case: Converts Python objects (not necessarily ORM objects) into Pydantic models by reading their attributes directly. 

        # from_orm = True # --> Use Case: When you are working with ORM (Object Relational Mapper) objects, such as SQLAlchemy, and want to convert them into a Pydantic model.

# all 3 methods can be used, for this example we are using 'form_attributes=True'


class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
