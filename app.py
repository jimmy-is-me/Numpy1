import streamlit as st

# 初始化 session_state
if 'step' not in st.session_state:
    st.session_state.step = 0

# 步驟 1：歡迎與引導
if st.session_state.step == 0:
    st.title("滇洱古韻 AI 推薦系統")
    st.write("歡迎來到滇洱古韻！請問您希望獲得專屬茶葉推薦嗎？")
    step1 = st.radio("選擇：", ["是的，幫我推薦適合的茶！", "我想先了解不同的茶款"])
    if step1:
        st.session_state.step = 1 if step1 == "是的，幫我推薦適合的茶！" else 2

# 步驟 2：口感偏好選擇
if st.session_state.step == 1:
    st.write("請問您喜歡哪種茶葉風味？")
    flavor = st.radio("選擇：", ["濃厚醇厚，帶有熟果香氣", "清甜回甘，口感鮮爽"])
    if flavor:
        st.session_state.step = 3

# 步驟 3：推薦茶品
if st.session_state.step == 3:
    if flavor == "濃厚醇厚，帶有熟果香氣":
        st.success("推薦您試試【熟普洱 A】與【熟普洱 B】。")
    else:
        st.success("推薦您試試【生普洱 C】與【生普洱 D】。")
    st.session_state.step = 4

# 步驟 4：試飲或購買
if st.session_state.step == 4:
    choice = st.radio("您希望怎麼體驗這款茶？", ["我要現場試飲看看", "直接購買"])
    if choice:
        st.session_state.step = 5
 
# 步驟 5：試飲後回饋
if st.session_state.step == 5:
    feedback = st.radio("請問您對試飲的茶品感覺如何？", ["很喜歡！我要了解更多", "還不錯，但想試試其他口味", "這款不太適合我"])
    if feedback:
        st.session_state.step = 0  # 重置步驟，開始新一輪互動
