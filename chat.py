import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

response = openai.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "您是一位有幫助的助手。"},
        {"role": "user", "content": "您好！"}
    ]
)

print(response.choices[0].message['content'])


