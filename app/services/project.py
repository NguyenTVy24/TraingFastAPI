from sqlalchemy.orm import Session

from app.schemas.project import ProjectBase
from ..crud import project
from app.services.user import UserService


class ProjectService:
    def __init__(self, db: Session):
        self.db = db

    async def creat_project(self, id_user: str, projectbase: ProjectBase):
        get_user = UserService(db=self.db)
        user = get_user.get_user(id_user=id_user)
        if user == "Loi":
            return "User not found"
        crt_project = project.create_project(db=self.db, projectbase=projectbase, id_user=id_user)
        if not crt_project:
            return "LOi"
        return crt_project

    async def get_project(self, id_project: str):
        crt_user = project.get_project(db=self.db, id_project=id_project)
        if not crt_user:
            return "LOi"
        return crt_user

    async def get_all_project(self, skip: int, limit: int):
        crt_user = project.get_all_project(db=self.db, skip=skip, limit=limit)
        if crt_user == "LOI":
            return "Project not found"
        return crt_user

    async def update_project_by_id(self, id_project: str, id_user: str, project_update: ProjectBase):
        current_std = project.update_project(db=self.db, id_project=id_project,
                                             id_user=id_user,
                                             project_update=project_update)
        if current_std == "LOI":
            return "User not found"
        return current_std

    async def del_project_id(self, id_project: str):
        current_std = project.delete_project(db=self.db, id_project=id_project)
        if not current_std:
            return "LOI"
        return current_std