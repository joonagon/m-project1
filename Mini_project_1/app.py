import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("서울시의 모기")
st.header("서울시 기온에 따른 모기 발생 빈도 변화")

tab1, tab2, tab3 = st.tabs(['메인', '모기지수 그래프', '서울시 기온변화'])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("최근 몇 년새 모기가 여름이 아닌 때에도 보이는 경우가 자주 있습니다.")
        st.markdown("모기지수와 기온변화 그래프를 통해 모기가 주로 발생하는 시기의 변화를 파악하고자 합니다.")

    with col2:
        st.image("https://news.seoul.go.kr/welfare/files/2020/02/62cfc9f3f36041.41905113-1086x1536.jpg",
        caption = "<서울시 모기예보제>, 출처 : http://data.seoul.go.kr/dataList/OA-13285/S/1/datasetView.do#",
        width = 360)

with tab2:
    st.subheader('모기 개체수에 비례한 모기지수 그래프')
    # UTF-8 / CP-949
    # https://seong6496.tistory.com/269 
    df1 = pd.read_csv('./Mini_project_1/mosdata.csv', encoding='cp949')
    mosq_data = df1[:2517]
    mosq_data['모기지수 발생일'] = pd.to_datetime(mosq_data['모기지수 발생일'])
    mosq_data1 = mosq_data[:1141]
    mosq_data2 = mosq_data[1143:2517]
    st.markdown("서울시는 모기 개체수를 2016년 5월부터 관측해왔습니다.")
    st.markdown("그리고 2020년 2월 17일부터는 모기가 발생하는 장소를 물가, 주거지, 공원 세 분류의 장소로 나누어 세분화 시켰습니다.")
    see_data = st.expander('서울시 모기지수 데이터 상세보기')
    with see_data:
        st.dataframe(data=mosq_data)
    
    st.markdown("")
    
    st.line_chart(data=mosq_data2,                                
                                  x='모기지수 발생일',
                                  y=['모기지수(수변부)','모기지수(주거지)','모기지수(공원)'],
                                  )
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