import openai
import os
import streamlit as st
from streamlit_chat import message

# 读取环境变量中的api_key
openai.api_key = os.environ.get("OPENAI_API_KEY")
# 也可直接写api_key
#openai.api_key  = 'API_KEY'

if 'prompts' not in st.session_state:
    st.session_state['prompts'] = [{"role": "system", "content": "您是一个乐于助人的助手。尽量简洁明了地回答问题，并带有一点幽默表达。"}]

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def generate_response(prompt):
    st.session_state['prompts'].append({"role": "user", "content": prompt})
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=st.session_state['prompts']
    )
    message = completion.choices[0].message.content
    return message

def end_click():
    st.session_state['prompts'] = [{"role": "system", "content": "您是一个乐于助人的助手。尽量简洁明了地回答问题，并带有一点幽默表达。"}]
    st.session_state['past'] = []
    st.session_state['generated'] = []
    st.session_state['user'] = ""

def chat_click():
    if st.session_state['user'] != '':
        chat_input = st.session_state['user']
        output = generate_response(chat_input)
        st.session_state['past'].append(chat_input)
        st.session_state['generated'].append(output)
        st.session_state['prompts'].append({"role": "assistant", "content": output})
        st.session_state['user'] = ""

st.image("./logo.png", width=80)
st.title("我的聊天机器人")

user_input = st.text_input("输入:", key="user")
chat_button = st.button("发送", on_click=chat_click)
end_button = st.button("新聊天", on_click=end_click)

if st.session_state['generated']:
    for i in range(0, len(st.session_state['generated']), 1):
        message(st.session_state['past'][i], is_user=True)
        message(st.session_state['generated'][i], key=str(i))
