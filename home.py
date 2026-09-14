import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.title(LAWS90286)

##store import variable in a session_state
if "name" not in st.session_state:
    st.session_state.button_value = False

##ask the user enter their name
st.header("Part 1 - Get Name")
name = st.text_input("What is your name?")

##if 
if name =="Jack":
    st.write("welcome")