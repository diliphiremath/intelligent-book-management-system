import os
from dotenv import load_dotenv
from app.config.db import engine
from groq import Groq
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase

# Load environment variables from the .env file
load_dotenv()

DATABASE_URL = os.getenv("LLM_DB")
# # Initialize LLM
# llm = Groq(
#     api_key = os.getenv("GROQ_API_KEY")
# )

db = SQLDatabase.from_uri(DATABASE_URL)
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name=os.getenv("MODEL"))
