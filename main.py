import streamlit as st

# ฟังก์ชันแสดงข้อความ
def display_message():
    st.markdown("Hello Viriya")

# ตั้งชื่อและคำอธิบาย
st.title("Hello Viriya")
st.write("test")
st.markdown(" ## my markdown")

# โค้ดที่ต้องการแสดง
code = '''
def hello():
    print("Hello Viriya")
'''

# สร้าง session state สำหรับการแสดงโค้ด
if "show_code" not in st.session_state:
    st.session_state.show_code = False

# ปุ่มแสดงโค้ด
if st.button("Show Code"):
    st.session_state.show_code = not st.session_state.show_code  # สลับค่า

if st.session_state.show_code:
    st.code(code, language='python')

# ปุ่มเรียกใช้ฟังก์ชัน
if st.button("Run"):
    display_message()
    st.session_state.show_code = False  # รีเซ็ตค่าเมื่อกด Run