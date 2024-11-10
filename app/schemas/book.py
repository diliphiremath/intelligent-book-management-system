from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    genre: Optional[str] = None
    year_published: Optional[int] = None
    summary: Optional[str] = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    class Config:
        orm_mode = True

class SummaryReview(BaseModel):
    summary: str
    rating: float
