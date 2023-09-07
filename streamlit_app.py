import streamlit as st
from PIL import Image
import pandas as pd
import random

df = pd.read_csv('동운아나텍_점심메뉴.csv')

image = Image.open('다운로드.png')
st.image(image)

st.write('동운아나텍 점심 메뉴 추천 페이지입니다.')
st.write('메뉴가 마음에 들지 않는다면 버튼을 다시 눌러보세요.')
st.write('\n')
st.write('점심 맛있게 드세요!')
st.write('\n')
col1, col2 = st.columns(2)

with col2:
    st.checkbox("상관없음")

with col1:
    menu = st.radio(
        "조건 선택 👇",
        ["한식만 추천", "중식만 추천", "일식만 추천", "양식만 추천", "베트남만 추천"],
    )
st.write('\n')
if st.button('점심 추천'):
    if menu == "한식만 추천":
        index = random.randrange(17,len(df))
        st.write('오늘의 점심은:')
        st.write(df.iloc[index,1] + '(' + df.iloc[index,0] + ')')
    else:
        index = random.randrange(0,len(df))
        st.write('오늘의 점심은:')
        st.write(df.iloc[index,1] + '(' + df.iloc[index,0] + ')')
st.write('\n')
st.write('\n')
if st.button('전체 메뉴 리스트'):
    st.write(pd.DataFrame(df))
st.write('\n')
st.write('맛집 추천 및 관련 문의는 박세일 주임에게 연락 부탁드립니다.')
