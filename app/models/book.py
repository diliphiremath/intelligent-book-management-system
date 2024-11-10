from sqlalchemy import Column, Integer, String, Text
from app.database.db import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=True)
    year_published = Column(Integer, nullable=True)
    summary = Column(Text, nullable=True)
