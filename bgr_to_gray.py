import streamlit as st
import cv2
import numpy as np
st.title("Convert Your Image to Gray Scale")
uploaded_file=st.file_uploader("Upload an image",type=['jpg','png'])
option=st.selectbox("Choose an option",['Show','Save'])
if st.button("Done"):
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        if option=="Show":
            st.subheader("Grayscale Image")
            st.image(gray, clamp=True, channels="GRAY")
        else:
            success, buffer = cv2.imencode(".png", gray)
    if success:
        st.download_button(
            label="⬇️ Download Grayscale Image",
            data=buffer.tobytes(),
            file_name="grayscale_image.png",
            mime="image/png"
        )
            st.success("Image downloaded successfully")

    else:
        st.warning("Image not uploaded successfully")


