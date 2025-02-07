import openai
import streamlit as st

# 從 Streamlit 的 secrets 中讀取 OpenAI API 金鑰
openai.api_key = st.secrets["openai"]["api_key"]

# 初始化聊天記錄
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "您是一位有幫助的助手。"}]

# 顯示聊天訊息
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 接收使用者輸入
if prompt := st.chat_input("請輸入您的訊息："):
    # 顯示使用者訊息
    st.chat_message("user").markdown(prompt)
    # 將使用者訊息加入聊天記錄
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 呼叫 OpenAI API 生成回應
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )
    # 取得並顯示助手回應
    assistant_message = response.choices[0].message.content
    st.chat_message("assistant").markdown(assistant_message)
    # 將助手回應加入聊天記錄
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
