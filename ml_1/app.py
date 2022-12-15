import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.float_format = '{:.2f}'.format
st.title("머신러닝 1")

df = pd.read_csv('https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/insurance.csv')
st.write(df)

import joblib
import os

model_path = f"{os.path.dirname(os.path.abspath(__file__))}/first_model.pkl"
model = joblib.load(model_path)
st.write("## 선형 회귀 모델")
st.write(pd.Series(model.coef_, index=["age", "bmi", "children", "smoker", "sex_male", "region_northwest", "region_northeast", "region_southwest"]))

# age : 나이
st.number_input(
    label = '나이',
    step=1,
    value=30,
    key='age'
)
#st.session_state['age']
#st.wirte(st.session_state['age'])


# sex : 성별
st.radio(
    label='성별'
    options=['남성', '여성'],
    index=0
    key='sex'
)
st.wirte(st.session_state['sex'])


# bmi : 실수형'
st.number_input(
    label = 'BMI',
    step=0.1,  ## 실수형으로 값을 받을수 있도록
    value=25,
    key='bmi'
)
st.wirte(st.session_state['bmi'])