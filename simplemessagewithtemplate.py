from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


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

if __name__ == "__main__":
    result = chain.invoke({
        "language": "Turkish",
        "text": "Hello,my name is Nejat. I am a software engineer."
    })
    print(result)