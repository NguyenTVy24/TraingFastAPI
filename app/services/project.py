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
