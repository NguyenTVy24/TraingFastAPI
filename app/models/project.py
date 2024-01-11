from sqlalchemy import Column, String , ForeignKey
from app.db.cndatabase import Base
from sqlalchemy.orm import relationship


class Project(Base):
    __tablename__ = "projects"
    id = Column(String, primary_key=True, index=True)
    description = Column(String)
    id_user = Column(String, ForeignKey("user.id"))

    user = relationship("User", back_populates="project")