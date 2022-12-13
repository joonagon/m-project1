import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write("http://data.seoul.go.kr/dataList/OA-13285/S/1/datasetView.do#")

df = pd.read_csv('./opendata/data.csv', encoding='cp949')
st.write(df)