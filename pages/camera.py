import streamlit as st
from PIL import Image

#Start the camera
camera_image = st.camera_input("Camera")

if camera_image :
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to greyscale
    grey_img = img.convert("L")

    # Render the greyscale image to webpage
    st.image(grey_img)