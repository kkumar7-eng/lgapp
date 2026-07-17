from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.globals import set_debug

set_debug(True)

load_dotenv()

st.title("Ask Anything")

with st.sidebar:
    st.title("Provide your API Key")
    OPENAI_API_KEY = st.text_input("OPENAI_API_KEY",type="password")
if not OPENAI_API_KEY:
    st.info("Please provide your OpenAI API key to continue")
    st.stop()

llm = ChatOpenAI(model="gpt-4o")

question = st.text_input("Enter the question: ")

if question:
    response = llm.invoke(question)
    st.write(response.content)



