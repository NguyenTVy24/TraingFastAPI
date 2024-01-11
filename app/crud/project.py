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


def get_all_project(db: Session, skip: int, limit: int):
    users_response = db.query(Project).offset(skip).limit(limit).all()
    return users_response


def update_project(db: Session, id_project: str, id_user: str, project_update: project.ProjectBase):
    db_project = get_project(db=db, id_project=id_project)
    if db_project is None:
        return "LOI"
    db_project = Project(id=db_project.id, description=project_update.description, id_user=id_user)
    db.commit()
    return db_project


def delete_project(db: Session, id_project: str):
    db_user = db.query(Project).filter(Project.id == id_project).first()
    if db_user:
        db.delete(db_user)
    db.commit()
    return db_user
