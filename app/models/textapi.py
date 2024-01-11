from sqlalchemy import Column, String
from app.db.cndatabase import Base


class TextAPI(Base):
    __tablename__ = "textapi"
    id_cou = Column(String, primary_key=True, index=True)
    title = Column(String)