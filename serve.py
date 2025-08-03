from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o",
    temperature=0.1
)
# messages = [
#     SystemMessage(
#         content="Translate the following English text to Turkish'"
#     ),
#     HumanMessage(
#         content="Hello, how are you?"
#     )
# ]

systemprompt = "You are a professional translator. Translate the following text from English to {language}. Only provide the translation, nothing else."
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",systemprompt),("human", "{text}")
    ]
)

parser = StrOutputParser()

chain = prompt_template | model | parser

app = FastAPI(
    title="Translator App",
    description="An example FastAPI application using LangChain with OpenAI.",
    version="1.0.0"
)

add_routes(
    app, 
    chain,
    path="/chain")

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="localhost", port=8000)