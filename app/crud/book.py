from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate

def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()

def update_book(db: Session, book_id: int, book_data: dict):
    db.query(Book).filter(Book.id == book_id).update(book_data)
    db.commit()
    
def delete_book(db: Session, book_id: int):
    db.query(Book).filter(Book.id == book_id).delete()
    db.commit()
