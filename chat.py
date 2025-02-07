import openai
import streamlit as st

# 從 Streamlit 的 secrets 中讀取 OpenAI API 金鑰
openai.api_key = st.secrets["openai"]["api_key"]

from openai import OpenAI

# 建立 OpenAI 客戶端實例
client = OpenAI()

# 定義訊息
messages = [
    {"role": "system", "content": "您是一位有幫助的助手。"},
    {"role": "user", "content": "您好！"}
]

# 呼叫 API 以獲取回應
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)

# 取得並顯示助手的回應
assistant_message = response.choices[0].message.content
print(assistant_message)
