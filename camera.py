import streamlit as st
from PIL import Image
import io
st.title("App to conver image to gray scale")
uploaded_image = st.file_uploader("uplaod your file")
if uploaded_image:
    img=Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img,caption="Gray Image")
    gray_bytes = io.BytesIO()
    gray_img.save(gray_bytes, format="PNG")

    st.download_button(
        label="Download Gray Image",
        data=gray_bytes.getvalue(),
        file_name="gray_image.png",
        key="download_gray_image",
    )

with st.expander("Start Camera"):
    #starting camera
    camera_image=st.camera_input("Camera")

    if camera_image:
        #Creating a pillow instance
        img=Image.open(camera_image)
        # Converting the pillow image to gray scale
        gray_img= img.convert("L")
        #render the image in webpage
        st.image(gray_img)
        gray_bytes_camera = io.BytesIO()
        gray_img.save(gray_bytes_camera, format="PNG")

        st.download_button(
            label="Download Gray Image",
            data=gray_bytes_camera.getvalue(),
            file_name="gray_image_camera.png",
            key="download_gray_image_camera",
        )



