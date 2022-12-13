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
    "https://cdn.pixabay.com/photo/2022/01/13/07/06/house-6934544_960_720.jpg"
    )

