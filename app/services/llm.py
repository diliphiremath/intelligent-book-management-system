from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain.chains import create_sql_query_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from app.config.llm import llm, db
from app.schemas.book import BookBase

def get_book_recommendations(prompt:str):

    create_query = create_sql_query_chain(llm, db)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    execute_query = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)
    chain = create_query | execute_query
    result = chain.invoke({"question":prompt})
    print(result)
    return {"recommendation":str(result["output"])}

#     chat_completion = llm.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": f"Recommend books for a user where gener is {genre} and rating is {min_rating}",
#         }
#     ],
#     model="llama3-8b-8192",
# )

#     print(chat_completion.choices[0].message.content)
#     recommendations = f""" {chat_completion.choices[0].message.content} """
#     return {"recommendations":recommendations}

def generate_summary(book:BookBase):
    
    prompt_template = "the title of the book is {title} and author of book is {author}. Generate a book summary"
    prompt = PromptTemplate(input_variables=["title","author"], template=prompt_template)
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"title":book.title,"author":book.author})
    return {"summary":response}

    
    


