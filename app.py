# Step 1: 歡迎與引導
st.title("滇洱古韻 AI 推薦系統")
st.write("歡迎來到滇洱古韻！請問您希望獲得專屬茶葉推薦嗎？")
step1 = st.radio("選擇：", ["是的，幫我推薦適合的茶！", "我想先了解不同的茶款"])

# Step 2: 口感偏好選擇
if step1:
    if step1 == "我想先了解不同的茶款":
        st.info("生普洱：清甜回甘、鮮爽。熟普洱：濃厚醇厚、熟果香氣。")
    
    st.write("請問您喜歡哪種茶葉風味？")
    flavor = st.radio("選擇：", ["濃厚醇厚，帶有熟果香氣", "清甜回甘，口感鮮爽"])

    # Step 3: 推薦茶品
    if flavor:
        if flavor == "濃厚醇厚，帶有熟果香氣":
            st.success("推薦您試試【熟普洱 A】與【熟普洱 B】。")
        else:
            st.success("推薦您試試【生普洱 C】與【生普洱 D】。")

        # Step 4: 試飲或直接購買
        choice = st.radio("您希望怎麼體驗這款茶？", ["我要現場試飲看看", "直接購買"])
        if choice == "我要現場試飲看看":
            st.warning("請向門市人員出示此畫面，體驗現場試飲。")
        else:
            st.markdown("[立即購買](https://yourshoplink.com)")

# Step 5: 回饋收集
feedback = st.radio("請問您對試飲的茶品感覺如何？", ["很喜歡！我要了解更多", "還不錯，但想試試其他口味", "這款不太適合我"])
if feedback:
    if feedback == "很喜歡！我要了解更多":
        st.info("我們將提供更詳細的茶葉介紹。")
    elif feedback == "還不錯，但想試試其他口味":
        st.info("推薦您試試不同類型的普洱茶。")
    else:
        st.info("我們將根據您的喜好重新推薦。")
