from fastapi import APIRouter, Depends, HTTPException
from app.services import recommendation
from pydantic import BaseModel
from app.config.db import SessionLocal
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Recommendation(BaseModel):
    recommendation: str

router = APIRouter()

@router.get("/recommendations", response_model=Recommendation)
def recommend(db: Session = Depends(get_db)):
    return recommendation.get_book_recommendations(db, genre="Science Fiction", min_rating=4.0)
