import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base

# Load environment variables from the .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

Base = declarative_base()

# Create an asynchronous database engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Create a sessionmaker that will create AsyncSessions
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# @asynccontextmanager
async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session