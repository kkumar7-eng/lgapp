from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.globals import set_debug

set_debug(True)

load_dotenv()


# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o")

st.title("Ask Anything")

question = st.text_input("Enter the question: ")

if question:
    response = llm.invoke(question)
    st.write(response.content)



