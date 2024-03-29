from fastapi import APIRouter
from app.api.endpoints import textapi
from app.api.endpoints import user
from app.api.endpoints import project
from app.api.endpoints import notification
from app.api.endpoints import login
router = APIRouter()

router.include_router(login.router, tags=["login"])
router.include_router(textapi.router, tags=["textapi"])
router.include_router(user.router, tags=["user"])
router.include_router(project.router, tags=["project"])
router.include_router(notification.router, tags=["notification"])

