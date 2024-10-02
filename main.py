import streamlit as st
from zipfile import ZipFile

# ตั้งชื่อแอป
st.title("Image Uploader")

# อัปโหลดรูปภาพ
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# ถ้ามีการอัปโหลดรูปภาพ ให้แสดงผล
if uploaded_file is not None:
    # แสดงผลรูปภาพที่อัปโหลดโดยตรง
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    st.write("Image uploaded successfully!")