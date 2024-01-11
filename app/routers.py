from fastapi import APIRouter
from app.api.endpoints import textapi
from app.api.endpoints import user
from app.api.endpoints import project
router = APIRouter()

router.include_router(textapi.router, tags=["textapi"])
router.include_router(user.router, tags=["user"])
router.include_router(project.router, tags=["project"])