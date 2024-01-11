from typing import Union
from app.schemas import user
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.db.cndatabase import get_db
from app.services.user import UserService

router = APIRouter()


@router.post("/create_user/", response_model=user.User)
async def create_user(userbase: user.UserBase, db: Session = Depends(get_db)):
    std_service = UserService(db=db)
    std_response = await std_service.creat_user(userbase=userbase)
    return std_response


@router.get("/get_user/{id_user}")
async def get_user(id_user: str, db: Session = Depends(get_db)):
    std_service = UserService(db=db)
    std_response = await std_service.get_user(id_user=id_user)
    return std_response


@router.get("/get_all_user/")
async def get_all_user(id_user: str, db: Session = Depends(get_db)):
    std_service = UserService(db=db)
    std_response = await std_service.get_all_user()
    return std_response

