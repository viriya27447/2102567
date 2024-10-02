import streamlit as st
import h5py
import requests
import io

# ตั้งชื่อแอป
st.title("Read H5 File from URL and Display Datasets")

# URL ของไฟล์ H5
file_url = 'https://firebasestorage.googleapis.com/v0/b/project-5195649815793865937.appspot.com/o/keras_model.h5?alt=media&token=c75818c8-a1ed-485e-9d57-b934d1743517'  # เปลี่ยนเป็น URL ของไฟล์ H5

# ดาวน์โหลดไฟล์ H5
try:
    response = requests.get(file_url)
    response.raise_for_status()  # ตรวจสอบว่าการดาวน์โหลดสำเร็จ

    # เปิดไฟล์ H5 จากข้อมูลที่ดาวน์โหลด
    with h5py.File(io.BytesIO(response.content), 'r') as h5_file:
        # แสดงรายการ datasets ในไฟล์
        st.write("Datasets in the H5 file:")
        for dataset in h5_file.keys():
            st.write(dataset)

except Exception as e:
    st.error(f"An error occurred: {e}")
