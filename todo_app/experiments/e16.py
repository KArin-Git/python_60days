import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.subheader('Color to Grayscale Converter')

uploaded_image = st.file_uploader('Upload Image')

with st.expander('Start camera'):
    camera_img = st.camera_input('Camera')

# check if camera is use and has img
if camera_img:
    img = Image.open(camera_img)
    gray_img = img.convert('L')
    st.image(gray_img)

# check if user upload a file
if uploaded_image:
    img = Image.open(uploaded_image)
    gray_uploaded_img = img.convert('L')
    st.image(gray_uploaded_img)
