from fastapi import FastAPI
from app.api.v1.endpoints import books, llm, users
from app.config.db import engine, Base
import asyncio

# Initialize the app
app = FastAPI()

# Event handler to create tables on startup
# @app.on_event("startup")
# async def startup_event():
#     async with engine.begin() as conn:
#         # Run schema creation if necessary
#         await conn.run_sync(Base.metadata.create_all)

app.include_router(books.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(llm.router, prefix="/api/v1")
