import streamlit as st
import openai

# 设置 OpenAI API 密钥
openai.api_key = st.secrets["openai_api_key"]

st.title("ChatGPT 聊天机器人")

# 初始化聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示聊天记录
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 获取用户输入
if prompt := st.chat_input("请输入您的问题："):
    # 显示用户消息
    with st.chat_message("user"):
        st.markdown(prompt)
    # 将用户消息添加到聊天记录
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用 OpenAI API 获取回复
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages,
    )

    # 获取助手的回复内容
    assistant_message = response.choices[0].message["content"]

    # 显示助手消息
    with st.chat_message("assistant"):
        st.markdown(assistant_message)
    # 将助手消息添加到聊天记录
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
