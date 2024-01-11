from fastapi import APIRouter
from app.api.endpoints import textapi

router = APIRouter()

router.include_router(textapi.router, tags=["textapi"])
