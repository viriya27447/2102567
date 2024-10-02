import streamlit as st
import requests
import io
import h5py

# ตั้งชื่อแอป
st.title("Upload H5 File from Google Drive")

# ให้ผู้ใช้กรอก ID ของไฟล์ H5
file_id = st.text_input("Enter the Google Drive file ID:")

# ถ้ามีการกรอก ID ให้ดำเนินการ
if file_id:
    try:
        # สร้าง URL สำหรับดาวน์โหลดไฟล์
        zip_url = f"https://drive.google.com/uc?id={file_id}"
        
        # ดึงข้อมูลจาก URL
        response = requests.get(zip_url)
        response.raise_for_status()  # ตรวจสอบว่าได้รับข้อมูลสำเร็จ

        # เปิดไฟล์ H5 จากข้อมูลที่ดาวน์โหลด
        with h5py.File(io.BytesIO(response.content), 'r') as h5_file:
            # แสดงชื่อของ datasets ในไฟล์ H5
            st.write("Datasets in the H5 file:")
            for dataset in h5_file.keys():
                st.write(dataset)

    except Exception as e:
        st.error(f"An error occurred: {e}")