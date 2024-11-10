from sqlalchemy.orm import Session
from app.models.review import Review
from app.models.book import Book

def get_summary_reviews(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
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