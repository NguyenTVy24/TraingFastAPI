from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..schemas.user import UserBase
from ..crud import user


class UserService:
    def __init__(self, db: Session):
        self.db = db

    async def creat_user(self, userbase: UserBase):
        crt_user = user.create_user(db=self.db, userbase=userbase)
        if not crt_user:
            return "LOi"
        return crt_user

    async def get_user(self, id_user: str):
        crt_user = user.get_user(db=self.db, id_user=id_user)
        if not crt_user:
            return "Loi"
        return crt_user

    async def get_all_user(self):
        crt_user = user.get_all_user(db=self.db)
        if not crt_user:
            return "Loi"
        return crt_user
