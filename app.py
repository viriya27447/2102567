# app.py
import streamlit as st
import pandas as pd
from viriya import ViriyaModel  # นำเข้าโมเดลจากไฟล์ viriya.py

# อินเตอร์เฟส Streamlit
st.title("Linear Regression Model with Viriya")

# อัพโหลดไฟล์ข้อมูล
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # อ่านข้อมูล
    data = pd.read_csv(uploaded_file)
    st.write("Data preview", data.head())

    # สร้างอินสแตนซ์ของโมเดล
    model = ViriyaModel()

    # เทรนโมเดลด้วยข้อมูลที่อัพโหลด
    model.train(data)

    # รับค่าอินพุตจากผู้ใช้
    feature1 = st.number_input('Input feature1')
    feature2 = st.number_input('Input feature2')

    if st.button('Predict'):
        # ใช้โมเดลทำนายค่า
        prediction = model.predict([feature1, feature2])
        st.write(f"Prediction: {prediction[0]}")