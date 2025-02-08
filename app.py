import streamlit as st
import openai

# 設定 OpenAI API 金鑰
openai.api_key = st.secrets["openai_api_key"]

st.title("ChatGPT 聊天機器人")

# 初始化聊天記錄
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "你是一個樂於助人的助手。"}]

# 顯示聊天記錄
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 獲取使用者輸入
if prompt := st.chat_input("請輸入您的問題："):
    # 顯示使用者消息
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 呼叫 OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5",  # 或使用 "gpt-3.5-turbo"
            messages=st.session_state.messages
        )
        assistant_message = response['choices'][0]['message']['content']

        # 顯示 AI 回覆
        with st.chat_message("assistant"):
            st.markdown(assistant_message)
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})

    except openai.error.OpenAIError as e:
        st.error(f"發生錯誤: {e}")
