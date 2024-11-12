from pydantic import BaseModel
from typing import Optional

class ReviewBase(BaseModel):
    user_id: int
    review_text: Optional[str] = None
    rating: int

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    book_id: int
    class Config:
        from_attributes = True
