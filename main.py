import streamlit as st

# ตั้งชื่อแอป
st.title("Addition Calculator")

# สร้างอินพุตให้ผู้ใช้ป้อนตัวเลขสองตัว
number1 = st.number_input("Enter first number:", value=0)
number2 = st.number_input("Enter second number:", value=0)

# ปุ่มคำนวณผลบวก
if st.button("Calculate"):
    # คำนวณผลลัพธ์
    result = number1 + number2
    # แสดงผลลัพธ์
    st.write("The sum is:", result)
