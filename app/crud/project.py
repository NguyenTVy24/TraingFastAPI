import uuid
from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas import project


def create_project(db: Session, id_user: str, projectbase: project.ProjectBase):
    id_tmp = str(uuid.uuid4())
    db_project = Project(id=id_tmp, description=projectbase.description, id_user=id_user)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_project(db: Session, id_project: str):
    user_response = db.query(Project).filter(Project.id == id_project).first()
    return user_response