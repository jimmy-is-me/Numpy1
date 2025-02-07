import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber 在紐約市的搭車數據分析')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename(lambda x: str(x).lower(), axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('正在加載數據...')
data = load_data(10000)
data_load_state.text('加載數據完成!')

if st.checkbox('顯示原始數據'):
    st.subheader('原始數據')
    st.write(data)

st.subheader('每小時搭車次數')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

st.subheader('所有搭車點地圖')
st.map(data)
