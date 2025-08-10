from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.chat_history import BaseChatMessageHistory,InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
import os


# Load environment variables from .env file
load_dotenv()

model = ChatOpenAI(model="gpt-4o")

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Answer all questions to the best of your ability."),
        MessagesPlaceholder(variable_name="messages")
    ])

chain = prompt | model
config = {"configurable" : {"session_id": "nejo"}}
with_history = RunnableWithMessageHistory(chain, get_session_history)

if __name__ == "__main__":
    while True:
        user_input = input(">")
        for r in with_history.stream(
            [
                HumanMessage(content=user_input)
            ],
            config=config
        ):
            print(r.content, end='')  # 
            
    # # Print session history
    #     session_history = get_session_history("nejo")
    #     print("\n--- Session History ---")
    #     for i, message in enumerate(session_history.messages):
    #         if isinstance(message, HumanMessage):
    #             print(f"{i+1}. Human: {message.content}")
    #         elif isinstance(message, AIMessage):
    #             print(f"{i+1}. AI: {message.content}")
    #     print("--- End History ---\n")