import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.title("SAGE")
st.caption("Your Smart Assistant for General Engineering")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask SAGE anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        history = [
            {"role": m["role"], "parts": [{"text": m["content"]}]}
            for m in st.session_state.messages[:-1]
        ]
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=history + [{"role": "user", "parts": [{"text": prompt}]}],
            config={
                "system_instruction": """You are SAGE (Smart Assistant for General Engineering).
                You are a personal AI assistant helping a software engineering graduate learn
                and grow. You are knowledgeable, encouraging, and explain things clearly.
                When explaining concepts, use simple language and real world examples.
                When helping with code, explain what each part does and why."""
            }
        )
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})