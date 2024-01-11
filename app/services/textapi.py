from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..schemas.textapi import TextApiBase
from ..crud.textapi import create_textapi

class TextApiService:
    def __init__(self, db: Session):
        self.db = db

    async def creat_textapi(self, textapi: TextApiBase):
        crt_textapi = create_textapi(db=self.db, textapi=textapi)
        if not crt_textapi:
            return "LOi"
        return crt_textapi