from app.schemas import project
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.db.cndatabase import get_db
from app.services.project import ProjectService
from app.api.depend import oauth2

router = APIRouter()


@router.post("/create_project/", response_model=project.Project)
async def create_user(projectbase: project.ProjectBase,
                      id_user: str,
                      db: Session = Depends(get_db),
                      decode_access_token=Depends(oauth2.verify_access_token)):
    std_service = ProjectService(db=db)
    std_response = await std_service.creat_project(projectbase=projectbase, id_user=id_user)
    return std_response


@router.get("/get_project/{id_project}")
async def get_user(id_project: str,
                   db: Session = Depends(get_db),
                   decode_access_token=Depends(oauth2.verify_access_token)):
    std_service = ProjectService(db=db)
    std_response = await std_service.get_project(id_project=id_project)
    return std_response


@router.get("/get_all_project/")
async def get_all_user(skip: int, limit: int,
                       db: Session = Depends(get_db),
                       decode_access_token=Depends(oauth2.verify_access_token)):
    std_service = ProjectService(db=db)
    std_response = await std_service.get_all_project(skip=skip, limit=limit)
    return std_response


@router.put("/update_project_by_id/{id_project}", response_model=project.Project)
async def update_project_by_id(id_project: str,
                               id_user: str,
                               project_update: project.ProjectBase,
                               db: Session = Depends(get_db),
                               decode_access_token=Depends(oauth2.verify_access_token)):
    std_service = ProjectService(db=db)
    std_response = await std_service.update_project_by_id(id_project=id_project,
                                                          id_user=id_user,
                                                          project_update=project_update)
    return std_response


@router.delete("/delete_project_by_id/{id_project}", response_model=project.Project)
async def delete_user(id_project: str,
                      db: Session = Depends(get_db),
                      decode_access_token=Depends(oauth2.verify_access_token)):
    project_connect = ProjectService(db=db)
    del_project = await project_connect.del_project_id(id_project=id_project)
    return del_project
