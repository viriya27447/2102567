import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# โหลดโมเดลจากไฟล์ .h5
model = load_model('your_model.h5')

# กำหนดฟังก์ชันสำหรับประมวลผลรูปภาพ
def preprocess_image(image):
    # เปลี่ยนขนาดภาพให้ตรงกับขนาดที่โมเดลรับ
    size = (224, 224)  # ขนาดที่โมเดลรับ (เช่น 224x224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    
    # แปลงภาพให้เป็น numpy array
    image = np.asarray(image)
    
    # ทำการ normalize (ถ้าจำเป็น) เช่นหารด้วย 255.0
    image = image.astype(np.float32) / 255.0
    
    # เพิ่มมิติใหม่เพื่อให้ตรงกับ input ของโมเดล (batch size, height, width, channels)
    image = np.expand_dims(image, axis=0)
    
    return image

# ฟังก์ชันทำนายผล
def predict(image):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    return prediction

# ส่วนของเว็บแอป
st.title("Image Classification App")

# อัพโหลดรูปภาพ
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # แสดงภาพที่อัพโหลด
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # ทำนายเมื่อกดปุ่ม
    if st.button('Predict'):
        st.write("Classifying...")
        prediction = predict(image)
        
        # แสดงผลการทำนาย
        st.write(f'Prediction: {np.argmax(prediction)}')
        st.write(f'Confidence: {np.max(prediction)}')

