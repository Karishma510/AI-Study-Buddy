import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

def query(prompt):
    response = model.generate_content(prompt)
    return response.text

st.title("AI Study Buddy")

option = st.selectbox(
    "Choose an option",
    ["Explain topic", "Summarize notes", "Generate quiz"]
)

text = st.text_area("Enter your text")

if st.button("Generate"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        with st.spinner("AI is thinking..."):
            if option == "Explain topic":
                prompt = f"Explain this topic in simple bullet points:\n{text}"
            elif option == "Summarize notes":
                prompt = f"Summarize these notes briefly:\n{text}"
            else:
                prompt = f"Create 5 quiz questions with answers from this text:\n{text}"

            result = query(prompt)
            st.success("Result")
            st.write(result)