import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("서울시의 모기 방역")
st.header("서울시의 모기 방역 이전과 이후")


st.image("https://news.seoul.go.kr/welfare/files/2020/02/62cfc9f3f36041.41905113-1086x1536.jpg")
st.write("http://data.seoul.go.kr/dataList/OA-13285/S/1/datasetView.do#")



# UTF-8 / CP-949
# https://seong6496.tistory.com/269
df1 = pd.read_csv('./Mini_project_1/mosdata.csv', encoding='cp949')
mosq_data = df1[:2517]
mosq_data

# st.line_chart(data=None, x=None, y=None, width=0, height=0, use_container_width=True
st.line_chart(data=mosq_data, x='모기지수 발생일', 
                              y=['모기지수(수변부)','모기지수(주거지)','모기지수(공원)'])

# 날씨 자료 링크(기상청) https://data.kma.go.kr/climate/RankState/selectRankStatisticsDivisionList.do

weather_data = pd.read_csv('./Mini_project_1/weather.csv', encoding='cp949')

weather_data

st.line_chart(data=weather_data, x='일시', y='평균기온(℃)')