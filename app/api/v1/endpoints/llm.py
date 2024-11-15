from app.schemas.book import Book
from app.services.auth import authenticate
from fastapi import APIRouter, Depends, HTTPException
from app.services import llm
from pydantic import BaseModel

class Recommendation(BaseModel):
    recommendation: str

class Summary(BaseModel):
    summary: str

router = APIRouter()

@router.get("/recommendations", response_model=Recommendation, dependencies=[Depends(authenticate)] )
def recommend(prompt:str):
    return llm.get_book_recommendations(prompt)

@router.post("/generate_summary", response_model=Summary, dependencies=[Depends(authenticate)])
def generate_summary(book: Book):
    return llm.generate_summary(book)
