from app.models.review import Review
from app.schemas.review import ReviewCreate
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

async def create_review(db: AsyncSession, review: ReviewCreate, book_id: int):
    db_review = Review(**review.dict(), book_id=book_id)
    db.add(db_review)
    await db.commit()
    await db.refresh(db_review)
    return db_review

async def get_reviews(db: AsyncSession, book_id: int):
    result = await db.execute(select(Review).where(Review.book_id  == book_id))
    return result.scalars().all()
