import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("머신러닝 2 - 로지스틱 회귀")

st.header('타이타닉 자료 기반 생존확률 예측')
ttsrv = pd.read_csv("https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/titanic_test.csv", 
                   index_col = "PassengerId")
st.write(ttsrv)

def pre_processing(df):
  
  ## 1,2,3,4 하고 info를 해보면 Fare 결측치가 하나 남음, 이걸처리함
  df.Fare = df.Fare.fillna(0)

  ## 1.결측치 embarked를 S로 채움
  df.Embarked=df.Embarked.fillna('S')

  ## 2.결측치 age를 title 기준의 평균값으로 채움
  df['Title'] = df.Name.str.extract('([A-Za-z])+\.')
  rarelist = (df.Title.value_counts() < 10).index.to_list()
  df.Title = df.Title.replace(rarelist, 'Rare')
  title_age_mean = df.groupby(['Title']).Age.mean()
  
  for v in df.Title.unique():
    df.loc[df.Age.isnull() & (df.Title == v),'Age'] = title_age_mean[v]
      
  ## 3.cabin, ticket, name, title 처럼 관계없는 열 드롭
  df.drop(columns=['Name','Ticket','Title','Cabin'],inplace = True)

  ## 4.범주형 변수는 pd.get_dummies 로 해결
  return pd.get_dummies(df, columns=['Sex','Embarked'],drop_first=True)

dttsrv = pre_processing(ttsrv)


#훈련셋, 시험셋
from sklearn.model_selection import train_test_split

X = dttsrv.drop('Survived', axis=1)
y = dttsrv['Survived']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=16)


#모델링
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)

pred = model.predict(X_test)
pred_proba = model.predict_proba(X_test)

#평가
LrSrv = pd.Series(model.coef_[0], index = X.columns)
st.wirte(LrSrv)

st.write("## 로지스틱 회귀 모델")

