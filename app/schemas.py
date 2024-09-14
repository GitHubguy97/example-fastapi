from pydantic import BaseModel, EmailStr, conint, Field
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mod = True #Don't need this code but tutorial did it.


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mod = True #Don't need this code but tutorial did it.

class UserCreate(BaseModel):
    email: EmailStr #validate email
    password: str



    class Config:
        orm_mod = True #Don't need this code but tutorial did it.


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0,le=1)