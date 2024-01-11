from pydantic import BaseModel


class ProjectBase(BaseModel):
    description: str
    id_user: str


class Project(ProjectBase):
    id: str

    class Config:
        orm_mode = True
