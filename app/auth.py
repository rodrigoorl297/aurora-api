from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.config import settings

oauth2 = OAuth2PasswordBearer(tokenUrl="auth/login")
ALGORITHM = "HS256"


def create_token(subject: str) -> str:
    exp = datetime.now(timezone.utc) + timedelta(hours=8)
    return jwt.encode({"sub": subject, "exp": exp}, settings.secret_key, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2)) -> str:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
        user = payload.get("sub")
        if not user:
            raise JWTError("missing sub")
        return str(user)
    except JWTError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token") from exc
