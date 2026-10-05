import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_gemini_response(query):
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=query
    )
    return response.text


st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.header("AI Chatbot")

user_input = st.text_input(
    "Enter your query here",
    key="input"
)

submit = st.button("Submit")

if submit:
    if user_input:
        response = get_gemini_response(user_input)
        st.write(response)
    else:
        st.write("Please enter a query.")