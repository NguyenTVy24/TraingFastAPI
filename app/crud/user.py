import uuid
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas import user


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


def get_all_user(db: Session):
    users_response = db.query(User)
    return users_response
