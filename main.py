import streamlit as st
import h5py

# ตั้งชื่อแอป
st.title("Read H5 File and Display Datasets")

# กำหนดที่อยู่ของไฟล์ H5 ที่จะอ่าน
file_path = 'D:\keras_model.h5'  # เปลี่ยนเป็นชื่อไฟล์ของคุณ

# เปิดไฟล์ H5
try:
    with h5py.File(file_path, 'r') as h5_file:
        # แสดงรายการ datasets ในไฟล์
        st.write("Datasets in the H5 file:")
        for dataset in h5_file.keys():
            st.write(dataset)

except Exception as e:
    st.error(f"An error occurred: {e}")
