from typing import List
from app.services.auth import authenticate
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.book import Book, BookCreate, SummaryReview
from app.schemas.review import Review, ReviewCreate
from app.crud import book as crud_book, review as crud_review
from app.services import book as service_book
from app.config.db import get_async_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/books", response_model=Book, dependencies=[Depends(authenticate)])
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_async_db)):
    return await crud_book.create_book(db, book)

@router.get("/books", response_model=List[Book], dependencies=[Depends(authenticate)])
async def read_books(db: AsyncSession = Depends(get_async_db)):
    return await crud_book.get_books(db)

@router.get("/books/{book_id}", response_model=Book, dependencies=[Depends(authenticate)])
async def read_book(book_id: int, db: AsyncSession = Depends(get_async_db)):
    db_book = await crud_book.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/books/{book_id}", response_model=Book, dependencies=[Depends(authenticate)])
async def update_book(book_id: int, book: BookCreate, db: AsyncSession = Depends(get_async_db)):
    await crud_book.update_book(db, book_id, book.dict())
    return await crud_book.get_book(db, book_id)

@router.delete("/books/{book_id}", dependencies=[Depends(authenticate)])
async def delete_book(book_id: int, db: AsyncSession = Depends(get_async_db)):
    await crud_book.delete_book(db, book_id)
    return {"message": "Book deleted successfully"}

@router.post("/books/{book_id}/reviews", response_model=Review, dependencies=[Depends(authenticate)])
async def create_review(book_id: int, review: ReviewCreate, db: AsyncSession = Depends(get_async_db)):
    return await crud_review.create_review(db, review, book_id)

@router.get("/books/{book_id}/reviews", response_model=List[Review], dependencies=[Depends(authenticate)])
async def read_reviews(book_id: int, db: AsyncSession = Depends(get_async_db)):
    return await crud_review.get_reviews(db, book_id)

@router.get("/books/{book_id}/summary", response_model=SummaryReview, dependencies=[Depends(authenticate)])
async def read_summary_reviews(book_id: int, db: AsyncSession = Depends(get_async_db)):
    return await service_book.get_summary_reviews(db, book_id)
