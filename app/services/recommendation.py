from sqlalchemy.orm import Session
from app.config.llm import llm

def get_book_recommendations(db: Session, genre: str, min_rating: float, author: str = None):

    chat_completion = llm.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Recommend books for a user where gener is {genre} and rating is {min_rating}",
        }
    ],
    model="llama3-8b-8192",
)

    print(chat_completion.choices[0].message.content)
    recommendations = f""" {chat_completion.choices[0].message.content} """
    return {"recommendations":recommendations}
