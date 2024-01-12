from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.db.cndatabase import SessionLocal
from app.services.user import UserService
from app.api.depend import oauth2
from app.utils.response import make_response_object
from app.api.depend.oauth2 import create_access_token, create_refresh_token

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/auth/login/")
async def login(login_id: str, db: Session = Depends(get_db)):
    us_service = UserService(db=db)
    user_response = await us_service.login(login_id=login_id)

    if user_response is not None:
        created_access_token = create_access_token(data={"uid": login_id})
        created_refresh_token = create_refresh_token(data={"uid": login_id})
        return make_response_object(data=dict(access_token=created_access_token,
                                              refresh_token=created_refresh_token))
    return user_response


@router.post("/auth/decode_token/")
async def decode_token(decoded_token=Depends(oauth2.get_decode_token)):
    return decoded_token


@router.post("/auth/refresh_token/")
async def refresh_token(decode_refresh_token=Depends(oauth2.verify_refresh_token),
                        db: Session = Depends(get_db)):
    user_service = UserService(db=db)
    current_user = await user_service.get_user_by_id(decode_refresh_token['uid'])
    if not current_user:
        return "loi"
    created_access_token = create_access_token(data={"uid": decode_refresh_token['uid']})
    created_refresh_token = create_refresh_token(data={"uid": decode_refresh_token['uid']})
    return make_response_object(data=dict(access_token=created_access_token,
                                          refresh_token=created_refresh_token))
