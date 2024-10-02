import streamlit as st
import cv2
import numpy as np

st.title("Real-time Video Stream with Streamlit")

# สร้างพื้นที่สำหรับแสดงผลวิดีโอ
video_placeholder = st.empty()

# เปิดกล้องโดยใช้ OpenCV
cap = cv2.VideoCapture(0)  # 0 หมายถึงกล้องตัวแรกที่เชื่อมต่อ

# ตรวจสอบว่ากล้องถูกเปิดหรือไม่
if not cap.isOpened():
    st.write("Error: Could not open video stream.")

else:
    # วนลูปเพื่ออ่านและแสดงผลเฟรมจากกล้องแบบเรียลไทม์
    while True:
        ret, frame = cap.read()
        if not ret:
            st.write("Error: Could not read frame from camera.")
            break
        
        # แปลงภาพจาก BGR (ของ OpenCV) เป็น RGB (ที่ Streamlit ใช้)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # แสดงผลเฟรมใน Streamlit
        video_placeholder.image(frame, channels="RGB")

        # ถ้าต้องการหยุดแสดงผลให้กดปุ่ม stop
        if st.button('Stop'):
            break

# ปิดกล้องหลังจากหยุดการทำงาน
cap.release()
