# app.py

import streamlit as st
from calculator import add_numbers  # นำเข้าฟังก์ชันจากไฟล์ calculator.py

# สร้างส่วนติดต่อผู้ใช้บน Streamlit
st.title("Simple Addition App")

# รับอินพุตตัวเลขสองตัวจากผู้ใช้
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

# เมื่อผู้ใช้คลิกปุ่ม "Add"
if st.button("Add"):
    # เรียกใช้ฟังก์ชัน add_numbers เพื่อคำนวณผลลัพธ์
    result = add_numbers(num1, num2)
    # แสดงผลลัพธ์
    st.write(f"The result is: {result}")
