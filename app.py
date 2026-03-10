import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Chatbot")
st.write("Ask a question and the AI will respond.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask something...")

if prompt:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = client.responses.create(
                model="gpt-4.1-mini",
                input=prompt
            )

            reply = response.output_text

            st.markdown(reply)

    # Save assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )