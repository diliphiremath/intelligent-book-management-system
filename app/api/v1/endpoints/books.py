from typing import List
from app.services.auth import authenticate
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.book import Book, BookCreate, SummaryReview
from app.schemas.review import Review, ReviewCreate
from app.crud import book as crud_book, review as crud_review
from app.services import book as service_book
from app.config.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/books", response_model=Book, dependencies=[Depends(authenticate)])
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return crud_book.create_book(db, book)

@router.get("/books", response_model=List[Book], dependencies=[Depends(authenticate)])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_book.get_books(db, skip=skip, limit=limit)

@router.get("/books/{book_id}", response_model=Book, dependencies=[Depends(authenticate)])
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud_book.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/books/{book_id}", response_model=Book, dependencies=[Depends(authenticate)])
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    crud_book.update_book(db, book_id, book.dict())
    return crud_book.get_book(db, book_id)

@router.delete("/books/{book_id}", dependencies=[Depends(authenticate)])
def delete_book(book_id: int, db: Session = Depends(get_db)):
    crud_book.delete_book(db, book_id)
    return {"message": "Book deleted successfully"}

@router.post("/books/{book_id}/reviews", response_model=Review, dependencies=[Depends(authenticate)])
def create_review(book_id: int, review: ReviewCreate, db: Session = Depends(get_db)):
    return crud_review.create_review(db, review, book_id)

@router.get("/books/{book_id}/reviews", response_model=List[Review], dependencies=[Depends(authenticate)])
def read_reviews(book_id: int, db: Session = Depends(get_db)):
    return crud_review.get_reviews(db, book_id)

@router.get("/books/{book_id}/summary", response_model=SummaryReview, dependencies=[Depends(authenticate)])
def read_summary_reviews(book_id: int, db: Session = Depends(get_db)):
    return service_book.get_summary_reviews(db, book_id)
