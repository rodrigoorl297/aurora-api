from fastapi import APIRouter, HTTPException, status

from app.auth import create_token
from app.config import settings
from app.schemas import LoginIn, TokenOut

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenOut)
def login(body: LoginIn):
    if body.username != settings.demo_user or body.password != settings.demo_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="bad credentials")
    return TokenOut(access_token=create_token(body.username))
