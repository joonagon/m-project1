# streamlit 라이브러리 호출
import streamlit as st
import numpy as np
import pandas as pd



#st.write() 마크다운

st.title('조 추첨 페이지')
st.header('여러분의 참여를 환영합니다.')



# 추첨 대상인 13명의 이름을 넣을 위치
# 3x4 형태로 배치

tabs = st.tabs(['참가자', '조'])

columns =tabs[0].columns(4)
for idx, col in enumerate(columns):
    for idx2 in range(4) :
        col.text_input(f"조 추첨 대상 {idx+1 + idx2 *4}", key=f"n{idx+1 + idx2 *4}")

columns2=tabs[1].columns(4)
for idx, col in enumerate(columns2):
    for idx2 in range(4) :
        col.text_input(f"조 목록 {idx+1 + idx2 *4}", key=f"g{idx+1 + idx2 *4}")



# 13명이 소속 될 조 이름을 넣을 위치
#st.write(st.session_state)
#ss = pd.Series(st.session_state)
#ss2 = ss[ss.ne("")]
#st.write(ss2)

#n_idx = ss2.index.str.contains('n')
#n_data = ss2[n_idx]
#st.write(n_data)

#g_idx = ss2.index.str.contains('g')
#g_data = ss2[g_idx]
#st.write(g_data)

#n_rd = np.random.choice(n_data, len(n_data), replace=False)
#st.write(n_rd)
#g_rd = np.random.choice(g_data, len(g_data), replace=False)
#st.write(g_rd)

# 추첨 버튼

if st.button('추첨 시작!'):
    ss = pd.Series(st.session_state)
    ss2 = ss[ss.ne("")]
    #st.write(ss2)

    n_idx = ss2.index.str.contains('n')
    n_data = ss2[n_idx]
    #st.write(n_data)

    g_idx = ss2.index.str.contains('g')
    g_data = ss2[g_idx]
    #st.write(g_data)

    n_rd = np.random.choice(n_data, len(n_data), replace=False)
    #st.write(n_rd)
    g_rd = np.random.choice(g_data, len(g_data), replace=False)
    #st.write(g_rd)

# 13개의 짝을 지어서 표시해줄 그래픽
df = pd.DataFrame({"추첨 대상자 이름":n_rd, "조 이름":g_rd})
