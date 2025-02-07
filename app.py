import streamlit as st

st.title('滇洱古韻 AI 推薦系統')

# 步驟 1：歡迎與引導
if 'step' not in st.session_state:
    st.session_state.step = 1

if st.session_state.step == 1:
    st.write('歡迎來到滇洱古韻！請問您希望獲得專屬茶葉推薦嗎？')
    option = st.radio('請選擇：', ['是的，幫我推薦適合的茶！', '我想先了解不同的茶款'])
    if option == '是的，幫我推薦適合的茶！':
        st.session_state.step = 2
    else:
        st.session_state.step = 2

# 步驟 2：口感偏好選擇
if st.session_state.step == 2:
    st.write('請問您喜歡哪種茶葉風味？')
    option = st.radio('請選擇：', ['濃厚醇厚，帶有熟果香氣', '清甜回甘，口感鮮爽'])
    if option == '濃厚醇厚，帶有熟果香氣':
        st.write('推薦您試試【熟普洱 A】與【熟普洱 B】。')
    else:
        st.write('推薦您試試【生普洱 C】與【生普洱 D】。')
    st.session_state.step = 3

# 步驟 3：試飲或直接購買
if st.session_state.step == 3:
    st.write('您希望怎麼體驗這款茶？')
    option = st.radio('請選擇：', ['我要現場試飲看看', '直接購買'])
    if option == '我要現場試飲看看':
        st.write('請向門市人員出示此畫面，體驗現場試飲。')
    else:
        st.write('您可以點擊【立即購買】連結，將茶葉加入購物車。')
    st.session_state.step = 4

# 步驟 4：試飲後的回饋
if st.session_state.step == 4:
    st.write('請問您對試飲的茶品感覺如何？')
    option = st.radio('請選擇：', ['很喜歡！我要了解更多', '還不錯，但想試試其他口味', '這款不太適合我'])
    if option == '很喜歡！我要了解更多':
        st.write('AI 提供更詳細的茶葉介紹。')
    elif option == '還不錯，但想試試其他口味':
        st.write('AI 推薦不同類型的普洱。')
    else:
        st.write('AI 重新推薦，根據您的回應調整。')
    st.session_state.step = 1
