# Intelligent Book Management System

A RESTful API built with FastAPI, PostgreSQL, designed to manage books, reviews and generate summary using AI/LLM.

## Features

- **Book Management**: Create, read, update, and delete book records.
- **Review Management**: Add and retrieve reviews for specific books.
- **Summary Generation**: Generate summary based on Book name and Author.
- **Book Suggestion**: Suggest book based on user prompt.
- **Asynchronous Operations**: Uses async SQLAlchemy (`asyncpg` and `sqlalchemy[asyncio]`) for high-performance database interactions.
- **Environment-based Configuration**: Environment variables control app settings and database configuration.

## Prerequisites
1. Python 3.10+
2. Postgres DB: https://www.postgresql.org/
3. Groq API: https://groq.com/

# Setup
1. Clone the Repository
git clone https://github.com/diliphiremath/intelligent-book-management-system.git

2. Set Up Environment Variables
Create an .env file similar to env-example file and add the details

3. Create a virtual env:
python3 -m venv venv

4. Install the requirements:
pip install -r requirements.txt

4. Start the application:
fastapi dev app/main.py and in the browser open http://127.0.0.1:8000/

## API Endpoints

Swagger doc - http://127.0.0.1:8000/docs

## Testing

Run tests with:
pytest

## Updates coming soon
Docker support

## License
This `README.md` provides comprehensive instructions for setting up, running, and using your FastAPI application, making it easy for others to get started with your project. Adjust any placeholder text (like the GitHub repo URL) as necessary.
