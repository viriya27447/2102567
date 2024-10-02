import streamlit as st
import requests
import zipfile
import io

# ตั้งชื่อแอป
st.title("Upload ZIP from Google Drive")

# ให้ผู้ใช้กรอก URL ของไฟล์ ZIP
zip_url = st.text_input("Enter the Google Drive ZIP file URL:")

# ถ้ามีการกรอก URL ให้ดำเนินการ
if zip_url:
    try:
        # ดึงข้อมูลจาก URL
        response = requests.get(zip_url)
        response.raise_for_status()  # ตรวจสอบว่าได้รับข้อมูลสำเร็จ

        # เปิดไฟล์ ZIP จากข้อมูลที่ดาวน์โหลด
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            # แสดงรายชื่อไฟล์ภายใน ZIP
            file_list = zip_ref.namelist()
            
            # แสดงรายชื่อไฟล์
            st.write("Files in the ZIP:")
            for file_name in file_list:
                st.write(file_name)
    except Exception as e:
        st.error(f"An error occurred: {e}")