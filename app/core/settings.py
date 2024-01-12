from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    # Pusher
    PUSHER_APP_ID = "1739608"
    PUSHER_KEY = "0aa3224a23defa0fac21"
    PUSHER_SECRET = "3763dce67a510f3958bb"
    PUSHER_CLUSTER = "ap1"
    PUSHER_SSL = True

    # Channels
    GENERAL_CHANNEL: Optional[str] = "general-channel"
    ALL_CHANNEL: Optional[str] = "all-channel"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
