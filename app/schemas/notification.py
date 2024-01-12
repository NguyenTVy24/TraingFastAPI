from typing import Optional
from pydantic import BaseModel


class NotificationBase(BaseModel):
    data: Optional[dict] = None
    id_user: Optional[str] = None
    notification_type: Optional[str] = None

