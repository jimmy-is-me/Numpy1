import streamlit as st
import openai

# 設定 OpenAI API 金鑰
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("ChatGPT 聊天機器人")

# 初始化聊天記錄
if "messages" not in st.session_state:
    st.session_state.messages = []

# 顯示聊天記錄
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 處理使用者輸入
if prompt := st.chat_input("請輸入您的訊息"):
    # 顯示使用者訊息
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 呼叫 OpenAI API 獲取回應
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages,
    )

    assistant_message = response.choices[0].message["content"]

    # 顯示助手回應
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
    with st.chat_message("assistant"):
        st.markdown(assistant_message)
