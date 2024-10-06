from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL

import streamlit as st
import h5py
import requests
import io
import numpy as np

# ตั้งชื่อแอป
st.title("Read H5 File from URL and Display Datasets")

# URL ของไฟล์ H5
file_url = 'https://firebasestorage.googleapis.com/v0/b/project-5195649815793865937.appspot.com/o/coffee_Model.h5?alt=media&token=719c44f9-4e93-462c-a398-8240b4cc71a3'  # เปลี่ยนเป็น URL ของไฟล์ H5

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
