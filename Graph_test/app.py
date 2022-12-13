import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

st.write(
    ```
    # 탐색적 데이터 분석(Exploratory Data Analysis)과 그래프
    >**EDA**
    * 그래프, 통계 수치등을 활용해서 데이터를 파악하는 과정
    * 탐색적 데이터 분석 단계에서는 다양한 그래프가 나옴
    * 그래프는 데이터를 한눈에 파악하는데 도움을 줌(경향성 파악)
    1. 데이터의 구성
    1. 어떤 변수(피처)가 중요한가
    1. 어떻게 새로운 변수를 만들까
    * 모델링에 필요한 다양한 정보를 얻을 수 있다.
    * **모델링** : 변수들을 통해 답을 이끌어 내는 과정. 통계, 머신러닝, 딥러닝 등
        1. 어떤 변수를 넣을지
        1. 어떻게 변형 시켜야 하는가(결측치, 이상치 등)
        1. 전처리 -> 피처 엔지니어링
    ```
)