import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("머신러닝 2 - 로지스틱 회귀")

st.header('타이타닉 자료 기반 생존확률 예측')
df = pd.read_csv("https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/titanic_test.csv", 
                   index_col = "PassengerId")
st.write(df)

import joblib
import os
model_path = f"{os.path.dirname(os.path.abspath(__file__))}/submission.csv"
model = joblib.load(model_path)
st.write("## 로지스틱 회귀 모델")
st.write(pd.Series(model.coef_, index=["Pclass", "Age", "SibSp",
 "Parch", "Fare", "Sex", "Embarked_Q", "Embarked_S"]))

