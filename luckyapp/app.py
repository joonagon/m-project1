# streamlit 라이브러리 호출
import streamlit as st
import numpy as np



#st.write() 마크다운

st.title('조 추첨 페이지')
st.header('여러분의 참여를 환영합니다.')

# 추첨 대상인 13명의 이름을 넣을 위치
# 3x4 형태로 배치

tabs = st.tabs(['참가자', '조'])

columns = st.columns(4)
for idx, col in enumerate(columns):
    for idx2 in range(4) :
        col.text_input(f"조 추첨 대상 {idx+1 + idx2 *4}", key="n{idx+1 + idx2 *4}")

columns2=tabs[1].columns(4)
for idx, col in enumerate(columns):
    for idx2 in range(4) :
        col.text_input(f"조 목록 {idx+1 + idx2 *4}", key="g{idx+1 + idx2 *4}")

# 13명이 소속 될 조 이름을 넣을 위치
#st.write(st.session_state)
ss = pd.Series(st.session_state)
ss2 = ss[ss.ne("")]
st.write(ss2)

# 추첨 버튼


# 13개의 짝을 지어서 표시해줄 그래픽

