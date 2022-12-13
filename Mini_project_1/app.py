import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("서울시의 모기 예측하기")
st.header("서울시의 모기 발생 빈도 변화 파악")


st.image("https://news.seoul.go.kr/welfare/files/2020/02/62cfc9f3f36041.41905113-1086x1536.jpg")
st.write("http://data.seoul.go.kr/dataList/OA-13285/S/1/datasetView.do#")


# UTF-8 / CP-949
# https://seong6496.tistory.com/269
df1 = pd.read_csv('./Mini_project_1/mosdata.csv', encoding='cp949')
mosq_data = df1[:2517]
mosq_data

# st.line_chart(data=None, x=None, y=None, width=0, height=0, use_container_width=True
st.line_chart(data=mosq_data, x='모기지수 발생일',y='모기지수(수변부)')
st.line_chart(data=mosq_data, x='모기지수 발생일',y='모기지수(주거지)')
st.line_chart(data=mosq_data, x='모기지수 발생일',y='모기지수(공원)')


weather_data = pd.read_csv('./Mini_project_1/weather.csv', encoding='cp949')
tempr = weather_data
tempr[['일시', '평균기온(℃)']]
st.line_chart(data=tempr, x='일시', y='평균기온(℃)', width = 70)

#lp_2 = sns.lineplot(data=df2, x='모기지수 발생일',y='모기지수(주거지)')
#lp_3 = sns.lineplot(data=df2, x='모기지수 발생일',y='모기지수(공원)')
#plt.show()