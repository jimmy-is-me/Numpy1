import openai
import streamlit as st

# 設定 OpenAI API 金鑰
openai.api_key = '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'

# 初始化聊天記錄
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 顯示聊天記錄
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# 使用者輸入
if prompt := st.chat_input('請輸入您的訊息'):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

    # 呼叫 OpenAI API 生成回應
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )
    assistant_reply = response['choices'][0]['message']['content']
    st.session_state.messages.append({'role': 'assistant', 'content': assistant_reply})
    with st.chat_message('assistant'):
        st.markdown(assistant_reply)
