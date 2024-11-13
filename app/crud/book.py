from app.services.llm import generate_summary
from app.models.book import Book
from app.schemas.book import BookCreate
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

async def create_book(db: AsyncSession, book: BookCreate):
    book.summary = generate_summary(book)["summary"]
    db_book = Book(**book.dict())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book

async def get_book(db: AsyncSession, book_id: int):
    result = await db.execute(select(Book).where(Book.id == book_id))
    return result.scalars().first()

async def get_books(db: AsyncSession):
    result = await db.execute(select(Book))
    return result.scalars().all()

async def update_book(db: AsyncSession, book_id: int, update_data: dict):
    book = await get_book(db, book_id)
    if book:
        for key, value in update_data.items():
            setattr(book, key, value)
        await db.commit()
        await db.refresh(book)
    return book
    
async def delete_book(db: AsyncSession, book_id: int):
    book = await get_book(db, book_id)
    if book:
        await db.delete(book)
        await db.commit()
    return book
