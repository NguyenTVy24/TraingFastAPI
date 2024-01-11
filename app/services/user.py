from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..schemas.user import UserBase
from ..crud.user import create_user


class UserService:
    def __init__(self, db: Session):
        self.db = db

    async def creat_user(self, userbase: UserBase):
        crt_user = create_user(db=self.db, userbase=userbase)
        if not crt_user:
            return "LOi"
        return crt_user
