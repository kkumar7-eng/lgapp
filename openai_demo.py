from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o")

question = input("Enter the question: ")
response = llm.invoke(question)
print(response)


