import streamlit as st
import h5py

# ตั้งชื่อแอป
st.title("Upload H5 File")

# อัปโหลดไฟล์ H5
uploaded_file = st.file_uploader("Choose an H5 file...", type=["h5"])

# ถ้ามีการอัปโหลดไฟล์
if uploaded_file is not None:
    # เปิดไฟล์ H5
    with h5py.File(uploaded_file, 'r') as h5_file:
        # แสดงชื่อของ datasets ในไฟล์
        st.write("Datasets in the H5 file:")
        for dataset in h5_file.keys():
            st.write(dataset)