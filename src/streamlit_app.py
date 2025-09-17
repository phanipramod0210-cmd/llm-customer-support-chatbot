import streamlit as st
from src.chatbot import answer
st.title('Customer Support Chatbot (Starter)')
q = st.text_input('Ask a question')
if q:
    st.write(answer(q))
