from app.schemas.book import Book
from fastapi import APIRouter, Depends, HTTPException
from app.services import llm
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

class Summary(BaseModel):
    summary: str

router = APIRouter()

@router.get("/recommendations", response_model=Recommendation)
def recommend(prompt:str):
    return llm.get_book_recommendations(prompt)

@router.post("/generate_summary", response_model=Summary)
def generate_summary(book: Book):
    return llm.generate_summary(book)
