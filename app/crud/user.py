import uuid
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas import user


def create_user(db: Session, userbase: user.UserBase):
    id_tmp = str(uuid.uuid4())
    db_user = User(id=id_tmp, name=userbase.name, gpa=userbase.gpa, gmail=userbase.gmail)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
