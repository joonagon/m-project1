import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("서울시의 모기")
st.header("서울시 기온에 따른 모기 발생 빈도 변화")

tab1, tab2, tab3 = st.tabs(['메인', '모기지수 그래프', '서울시 기온변화'])

with tab1:
    st.image("https://news.seoul.go.kr/welfare/files/2020/02/62cfc9f3f36041.41905113-1086x1536.jpg")
    st.write("http://data.seoul.go.kr/dataList/OA-13285/S/1/datasetView.do#")

with tab2:
    st.subheader('모기 개체수에 비례한 모기지수 그래프')
    # UTF-8 / CP-949
    # https://seong6496.tistory.com/269 
    df1 = pd.read_csv('./Mini_project_1/mosdata.csv', encoding='cp949')
    mosq_data = df1[:2517]
    mosq_data['모기지수 발생일'] = pd.to_datetime(mosq_data['모기지수 발생일'])
    mosq_data1 = mosq_data[:1141]
    mosq_data2 = mosq_data[1143:2517]

    st.markdown("")
    see_data = st.expander('서울시 모기지수 데이터 상세보기')
    with see_data:
        st.dataframe(data=mosq_data)

    add_vertical_space()

    # st.line_chart(data=None, x=None, y=None, width=0, height=0, use_container_width=True
    st.line_chart(data=mosq_data2,                                
                                  x='모기지수 발생일',
                                  y=['모기지수(수변부)','모기지수(주거지)','모기지수(공원)'],
                                  )
    
    add_vertical_space()
    
    st.line_chart(data=mosq_data1,                                  
                                  x='모기지수 발생일',
                                  y=['모기지수(수변부)','모기지수(주거지)','모기지수(공원)'],
                                  )


with tab3:
    # 날씨 자료 링크(기상청) https://data.kma.go.kr/climate/RankState/selectRankStatisticsDivisionList.do
    st.subheader('서울시 기온변화 (2016 ~ )')

    weather_data = pd.read_csv('./Mini_project_1/extremum_20221214093542.csv', encoding='cp949', skiprows=10)
    weather_data2 = weather_data[['일시', '평균기온(℃)','최고기온(℃)','최저기온(℃)']]

    st.markdown("")
    see_data = st.expander('서울시 기온변화 상세보기(2016 ~ )')
    with see_data:
        st.dataframe(data=weather_data)


    st.line_chart(data=weather_data2, x='일시',
                                      y=['평균기온(℃)','최고기온(℃)','최저기온(℃)'])