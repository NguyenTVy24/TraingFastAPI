from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.notification import NotificationService
from app.schemas.notification import NotificationBase
from app.db.cndatabase import get_db

router = APIRouter()


@router.post("/notifications/", response_model=dict)
async def create_notification(request_data: NotificationBase, db: Session = Depends(get_db)):
    notification_service = NotificationService(db=db)
    a = await notification_service.create_notification(request_data)
    return NotificationBase
