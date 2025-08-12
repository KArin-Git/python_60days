import streamlit as st
from PIL import Image

# start camera
camera_image = st.camera_input('Camera')
# camera_image can be None while browser is asking for the camera permission
if camera_image:
    # create a Pillow img instance
    img = Image.open(camera_image)
    # convert the pillow img to grayscale
    gray_img = img.convert('L')
    # render the grayscale img on the webpage
    st.image(gray_img)