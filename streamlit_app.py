import streamlit as st
from PIL import Image
import pandas as pd

image = Image.open('다운로드.png')
st.image(image)

st.write('동운아나텍 점심식사 추천 페이지입니다.')
st.write('\n')
st.write('점심 맛있게 드세요!')
st.write('\n')
st.button('점심 추천')
st.write('\n')
st.write('\n')
st.write('전체 메뉴 리스트:')
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))
st.write('\n')
st.write('문의사항은 박세일 주임에게 연락주세요.')
