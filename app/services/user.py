from sqlalchemy.orm import Session

from app.schemas.project import ProjectBase
from app.schemas.user import UserBase
from app.crud import user
from app.core.exceptions import error_exception_handler
from app.constant.app_status import AppStatus


class UserService:
    def __init__(self, db: Session):
        self.db = db

    async def login(self, login_id: str):
        current_login = user.check_exits_id(db=self.db, login_id=login_id)
        if not current_login:
            raise error_exception_handler(error=Exception(), app_status=AppStatus.ERROR_ID_NOT_FOUND)
        return current_login

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

    async def get_user_by_id(self, id_user: str):
        current_user = user.get_user_and_project(db=self.db, id_user=id_user)
        if not current_user:
            return "LOI"
        return current_user

    async def get_all_user(self, skip: int, limit: int):
        crt_user = user.get_all_user(db=self.db, skip=skip, limit=limit)
        if not crt_user:
            return "Loi"
        return crt_user

    async def update_user_by_id(self, id_user: str, user_update: UserBase, project_update: ProjectBase):
        current_std = user.update_user(db=self.db, id_user=id_user,
                                       user_update=user_update,
                                       project_update=project_update)
        if current_std == "LOI":
            return "User not found"
        return current_std

    async def del_user_id(self, id_user: str):
        current_std = user.delete_user(db=self.db, id_user=id_user)
        if not current_std:
            return "LOI"
        return current_std
