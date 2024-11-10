from fastapi import FastAPI
from app.api.v1.endpoints import books
from app.database.db import engine, Base, get_db

# Initialize the app
app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(books.router, prefix="/api/v1")
