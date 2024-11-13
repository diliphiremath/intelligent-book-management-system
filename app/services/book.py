from app.models.review import Review
from app.models.book import Book
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

async def get_summary_reviews(db: AsyncSession, book_id: int):
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalars().first()
    summary = book.summary
    reviews = db.query(Review).filter(Review.book_id == book_id).all()
    total_rating = 0
    aggregated_rating = 0
    if len(reviews):
        for i in reviews:
            total_rating += i.rating
        aggregated_rating = total_rating/len(reviews)
    return {
        "summary":summary,
        "rating":aggregated_rating
    }