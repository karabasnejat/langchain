from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatOpenAI(
    model="gpt-4o",
    temperature=0.1
)
messages = [
    SystemMessage(
        content="Translate the following English text to Turkish'"
    ),
    HumanMessage(
        content="Hello, how are you?"
    )
]

parser = StrOutputParser()

chain = model | parser

if __name__ == "__main__":
    print(chain.invoke(messages))