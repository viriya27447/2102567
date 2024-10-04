import streamlit as st

# ตั้งชื่อแอป
st.title("Camera Input Example")

# ใช้งาน camera_input
image = st.camera_input("Take a picture")

if image is not None:
    st.image(image, caption="Captured Image", use_column_width=True)
    st.write(5+5)
