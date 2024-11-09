import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
    'dbname': 'bmsdb',
    'user': 'dilip',
    'password': '9',
    'host': 'localhost',
    'port': '5432'
}

def create_schema_and_tables(schema_name):
    try:
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(**db_params)
        conn.autocommit = True
        cursor = conn.cursor()

        # Create schema if it does not exist
        cursor.execute(sql.SQL("CREATE SCHEMA IF NOT EXISTS {}").format(
            sql.Identifier(schema_name)
        ))

        # SQL command to create the 'books' table within the specified schema
        create_books_table = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {}.books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            genre VARCHAR(100),
            year_published INT,
            summary TEXT
        );
        """).format(sql.Identifier(schema_name))

        # SQL command to create the 'reviews' table within the specified schema
        create_reviews_table = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {}.reviews (
            id SERIAL PRIMARY KEY,
            book_id INT REFERENCES {}.books(id) ON DELETE CASCADE,
            user_id INT NOT NULL,
            review_text TEXT,
            rating INT CHECK (rating >= 1 AND rating <= 5)
        );
        """).format(sql.Identifier(schema_name), sql.Identifier(schema_name))

        # Execute the table creation commands
        cursor.execute(create_books_table)
        cursor.execute(create_reviews_table)

        print(f"Tables 'books' and 'reviews' created successfully in schema '{schema_name}'.")
        
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

# Specify your schema name
schema_name = 'bms_schema'
create_schema_and_tables(schema_name)
