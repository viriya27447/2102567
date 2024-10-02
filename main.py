import streamlit as st
import zipfile
import os

# ตั้งชื่อแอป
st.title("ZIP File Reader")

# อัปโหลดไฟล์ ZIP
uploaded_file = st.file_uploader("Choose a ZIP file...", type=["zip"])

# ถ้ามีการอัปโหลดไฟล์ ZIP
if uploaded_file is not None:
    # สร้างชื่อไฟล์ ZIP
    with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
        # แสดงรายชื่อไฟล์ภายใน ZIP
        file_list = zip_ref.namelist()
        
        # แสดงรายชื่อไฟล์
        st.write("Files in the ZIP:")
        for file_name in file_list:
            st.write(file_name)
