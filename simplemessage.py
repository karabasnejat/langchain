from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage


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

if __name__ == "__main__":
    response = model.invoke(messages)
    print(response.content)