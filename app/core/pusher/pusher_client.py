import pusher
from app.core.singleton.singleton import Singleton
from app.core.settings import settings


class PusherClient(Singleton):
    def __init__(self):
        self.pusher_client = pusher.Pusher(
            app_id=settings.PUSHER_APP_ID,
            key=settings.PUSHER_KEY,
            secret=settings.PUSHER_SECRET,
            cluster=settings.PUSHER_CLUSTER,
            ssl=settings.PUSHER_SSL
        )

    def push_notification(self, channel, event, data_push):
        self.pusher_client.trigger(channel, event, data_push)
