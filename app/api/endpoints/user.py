from typing import Union
from app.schemas import user
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.db.cndatabase import SessionLocal, get_db
from app.services.user import UserService

router = APIRouter()


@router.post("/create_user/", response_model=user.User)
async def create_student(userbase: user.UserBase, db: Session = Depends(get_db)):
    std_service = UserService(db=db)
    std_response = await std_service.creat_user(userbase=userbase)
    return std_response
