import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write("http://data.seoul.go.kr/dataList/OA-13285/S/1/datasetView.do#")

# UTF-8 / CP-949
# https://seong6496.tistory.com/269
df = pd.read_csv('./Mini_project_1/mosdata.csv', encoding='cp949')
st.write(df)

df.describe()