import uuid
from sqlalchemy.orm import Session
from app.models.textapi import TextAPI
from app.schemas import textapi

def create_textapi(db: Session, textapi: textapi.TextApiBase):
    id_tmp = str(uuid.uuid4())
    db_textapi = TextAPI(id_cou=id_tmp, title=textapi.title)
    db.add(db_textapi)
    db.commit()
    db.refresh(db_textapi)
    return db_textapi