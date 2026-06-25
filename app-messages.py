import streamlit as st


# Options for chat_message parameter are: user, assistant, human, AI, system, and error
with st.chat_message("AI"):
    st.write("Hello there!")
    

prompt = st.chat_input("Type your message", max_chars = 50)
if prompt:
    st.write(f"User message: {prompt}")