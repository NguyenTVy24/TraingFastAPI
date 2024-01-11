from sqlalchemy import Column, String
from app.db.cndatabase import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "user"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    gpa = Column(String)
    gmail = Column(String)

    project = relationship("Project", back_populates="user")
