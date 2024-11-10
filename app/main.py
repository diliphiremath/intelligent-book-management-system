from fastapi import FastAPI
from app.api.v1.endpoints import books, users, recommendation
from app.config.db import engine, Base, get_db

# Initialize the app
app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(books.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(recommendation.router, prefix="/api/v1")
