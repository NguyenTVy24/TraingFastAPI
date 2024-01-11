import uuid
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.project import Project
from app.schemas import user
from app.schemas import project


def create_user(db: Session, userbase: user.UserBase):
    id_tmp = str(uuid.uuid4())
    db_user = User(id=id_tmp, name=userbase.name, gpa=userbase.gpa, email=userbase.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, id_user: str):
    user_response = db.query(User).filter(User.id == id_user).first()
    return user_response


def get_all_user(db: Session, skip: int, limit: int):
    users_response = db.query(User).offset(skip).limit(limit).all()
    return users_response


def update_user(db: Session, id_user: str, user_update: user.UserBase, project_update: project.ProjectBase):
    db_user = get_user(db=db, id_user=id_user)
    if db_user is None:
        return "User does not exist"
    db_project = db.query(Project).filter(Project.id_user == id_user).first()
    for field, value in user_update.dict().items():
        setattr(db_user, field, value)
    if db_project is None:
        return "Project does not exist"
    for field, value in project_update.dict().items():
        setattr(db_project, field, value)
    db.commit()
    db.refresh(db_user)
    db.refresh(db_project)
    return db_user, db_project

