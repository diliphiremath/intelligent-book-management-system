import os
from dotenv import load_dotenv
from app.config.db import engine
from groq import Groq

# Load environment variables from the .env file
load_dotenv()

# Initialize LLM
llm = Groq(
    api_key = os.getenv("GROQ_API_KEY")
)

# # Define a prompt template for the LLM to follow when generating recommendations
# prompt_template = PromptTemplate(
#     template="""
#     You are a book recommendation assistant. Given the user preferences, recommend books from the database.
#     User preferences:
#     - Genre: {genre}
#     - Minimum rating: {min_rating}
#     - Author preference (if any): {author}

#     Only recommend books that match these criteria and provide a short description for each.
#     if you dont get any books from database then return "I didn't find any books"
#     """,
#     input_variables=["genre", "min_rating", "author"]
# )
