import openai
import streamlit as st

openai.api_key = st.secrets["openai"]["api_key"]
