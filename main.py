import streamlit as st
import h5py

# ตั้งชื่อแอป
st.title("Read H5 File and Display Datasets")

# อัปโหลดไฟล์ H5

uploaded_file = '"D:\keras_model.h5"'
# ถ้ามีการอัปโหลดไฟล์
if uploaded_file is not None:
    # เปิดไฟล์ H5
    with h5py.File(uploaded_file, 'r') as h5_file:
        # แสดงชื่อของ datasets ในไฟล์
        st.write("Datasets in the H5 file:")
        for dataset in h5_file.keys():
            st.write(dataset)

        # ตัวอย่างการแสดงข้อมูลจาก dataset แรก
        if h5_file:
            first_dataset = next(iter(h5_file.keys()))  # ดึงชื่อ dataset แรก
            data = h5_file[first_dataset][:]
            st.write(f"Data from dataset '{first_dataset}':")
            st.write(data)
