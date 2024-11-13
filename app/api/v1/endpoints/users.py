from app.services.auth import authenticate
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas.user import User, UserCreate
from app.crud import user as crud_user
from app.config.db import get_async_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/users", response_model=User)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_async_db)):
    db_user = await crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await crud_user.create_user(db=db, user=user)

@router.get("/users", response_model=List[User], dependencies=[Depends(authenticate)])
async def read_users(db: AsyncSession = Depends(get_async_db)):
    return await crud_user.get_users(db)

@router.get("/users/{user_id}", response_model=User, dependencies=[Depends(authenticate)])
async def read_user(user_id: int, db: AsyncSession = Depends(get_async_db)):
    db_user = await crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
