from sqlalchemy.orm import Session
from app.core.pusher.pusher_client import PusherClient
from ..schemas.notification import NotificationBase
from app.core.settings import settings


class NotificationService:
    def __init__(self, db: Session):
        self.db = db

    async def create_notification(self, request_data: NotificationBase):
        client = PusherClient()
        client.push_notification(settings.GENERAL_CHANNEL, request_data.id_user, request_data.__str__())

