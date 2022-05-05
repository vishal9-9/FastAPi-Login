from pydantic import BaseModel
from typing import List,Optional

class login(BaseModel):
    username : str
    passwd : str

class show_login(BaseModel):
    email : str
    name : str
    class Config:
        orm_mode = True

class blog(BaseModel):
    title : str
    body : str
    class Config:
        orm_mode = True

class show_users(BaseModel):
    id : int
    name : str
    email : str
    blogs : List[blog]
    class Config:
        orm_mode = True

class show_blogs(BaseModel):
    title : str
    body : str
    class Config:
        orm_mode = True

class show_blogs_withid(BaseModel):
    id : int
    class Config:
        orm_mode = True

class get_blogs_withid(BaseModel):
    id : int


class create_users(BaseModel):
    name : str
    passwd : str
    email : str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None