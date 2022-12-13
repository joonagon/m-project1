# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 제 첫 웹페이지 입니다
    ## 부족하지만 잘부탁드립니다!
    * 1$ = 1300원
    """
)

# https://unsplash.com
# https://pixabay.com/ko
st.image(
    "https://images.unsplash.com/photo-1670873033664-023b830d17d2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=686&q=80"
)