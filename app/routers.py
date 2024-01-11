from fastapi import APIRouter
from app.api.endpoints import textapi
from app.api.endpoints import user
router = APIRouter()

router.include_router(textapi.router, tags=["textapi"])
router.include_router(user.router, tags=["user"])