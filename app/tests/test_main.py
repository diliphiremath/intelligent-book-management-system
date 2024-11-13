from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_create_book():
    # Add a new book with Basic Auth
    response = client.post(
        "/api/v1/books",
        json={
            "title": "Test Book",
            "author": "Author Name",
            "genre": "Fiction",
            "year_published": 2020,
            "summary": "A short summary of the book."
        },
        auth=("dom", "123456")
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"