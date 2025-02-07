import streamlit as st

st.title('聊天機器人')

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input('請輸入您的訊息'):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

    # 在此處加入您的聊天機器人邏輯，例如調用模型生成回應
    response = '這是機器人的回應'  # 替換為實際的回應生成邏輯

    st.session_state.messages.append({'role': 'assistant', 'content': response})
    with st.chat_message('assistant'):
        st.markdown(response)
