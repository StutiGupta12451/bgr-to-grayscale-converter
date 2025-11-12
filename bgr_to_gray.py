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
            cv2.imshow("Grayscale Image",gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            cv2.imwrite("grayscale.jpg",gray)
            st.success("Image downloaded successfully")

    else:
        st.warning("Image not uploaded successfully")
