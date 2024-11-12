from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.config.db import SessionLocal
from app.models.user import User

security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

USER_DATA = {
    "admin": pwd_context.hash("adminpassword"),
    "user": pwd_context.hash("userpassword"),
}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def authenticate(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = get_user_by_username(db, credentials.username)
    if user and verify_password(credentials.password, user.hashed_password):
        return user.username
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
