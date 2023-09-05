import streamlit as st
from PIL import Image

st.write('동운아나텍 점심식사 추천 페이지입니다.')
st.write('\n')
st.write('점심 맛있게 드세요!')
st.write('\n')
st.button('점심 추천')

image = Image.open('다운로드.png')

st.image(image)
