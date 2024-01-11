from typing import Optional

from pydantic import BaseModel

class TextApiBase(BaseModel):
    title: Optional[str] = None

class TextApi(TextApiBase):
    id_cou: str
    class Config:
        orm_mode = True