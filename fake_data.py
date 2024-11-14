import psycopg2
from psycopg2 import sql
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Database connection details
DB_NAME = "bmsdb2"
DB_USER = "admin"
DB_PASSWORD = "qwerty"
DB_HOST = "localhost"
DB_PORT = "5432"

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cur = conn.cursor()

# Function to create fake books
def insert_fake_books(num_records=50):
    book_ids = []
    for _ in range(num_records):
        title = fake.sentence(nb_words=4)
        author = fake.name()
        genre = fake.word(ext_word_list=["Science Fiction", "Fantasy", "Mystery", "Romance", "Non-Fiction", "Thriller"])
        year_published = random.randint(1900, 2023)
        summary = fake.paragraph(nb_sentences=3)
        
        cur.execute("""
            INSERT INTO books (title, author, genre, year_published, summary)
            VALUES (%s, %s, %s, %s, %s) RETURNING id;
        """, (title, author, genre, year_published, summary))
        
        # Retrieve the generated book ID
        book_id = cur.fetchone()[0]
        book_ids.append(book_id)
    
    return book_ids

# Function to create fake reviews
def insert_fake_reviews(book_ids, num_records=50):
    for _ in range(num_records):
        book_id = random.choice(book_ids)
        user_id = random.randint(1, 100)  # Example user ID
        review_text = fake.paragraph(nb_sentences=2)
        rating = random.randint(1, 5)
        
        cur.execute("""
            INSERT INTO reviews (book_id, user_id, review_text, rating)
            VALUES (%s, %s, %s, %s);
        """, (book_id, user_id, review_text, rating))

# Insert fake data
try:
    print("Inserting fake books...")
    book_ids = insert_fake_books()
    
    print("Inserting fake reviews...")
    insert_fake_reviews(book_ids)

    # Commit the transaction
    conn.commit()
    print("Data insertion complete.")
except Exception as e:
    print(f"An error occurred: {e}")
    conn.rollback()
finally:
    cur.close()
    conn.close()
