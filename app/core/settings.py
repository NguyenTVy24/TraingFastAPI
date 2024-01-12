from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):

    ACCESS_TOKEN_EXPIRES_IN_DAYS = 2
    REFRESH_TOKEN_EXPIRES_IN_DAYS = 2
    JWT_ALGORITHM = "HS256"
    JWT_SECRET_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY4MTY1NTk4OCwiaWF0IjoxNjgxNjU1OTg4fQ.ADE6 - duU6rK1uRwH9R8E59J7bsypHbDHefei5Lb2kdoHXHFY"

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
