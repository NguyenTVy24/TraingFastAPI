from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    gpa: str
    email: str


class User(UserBase):
    id: str

    class Config:
        orm_mode = True
