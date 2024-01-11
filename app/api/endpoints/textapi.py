from typing import Union
from app.schemas import textapi
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.db.cndatabase import SessionLocal, get_db
from app.services.textapi import TextApiService
router = APIRouter()


@router.post("/create_textapi/", response_model=textapi.TextApi)
async def create_student(textapi: textapi.TextApiBase, db: Session = Depends(get_db)):
    std_service = TextApiService(db=db)
    std_response = await std_service.creat_textapi(textapi=textapi)
    return std_response


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
