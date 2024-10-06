import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# ฟังก์ชันสำหรับโหลดโมเดล
@st.cache(allow_output_mutation=True)
def load_model(model_file):
    model = tf.keras.models.load_model(model_file)
    return model

# ฟังก์ชันสำหรับแปลงภาพเป็นรูปแบบที่โมเดลต้องการ
def preprocess_image(image, target_size):
    image = image.resize(target_size)
    image = np.array(image)
    image = image / 255.0  # Normalize ให้ค่าอยู่ในช่วง 0-1
    image = np.expand_dims(image, axis=0)  # เพิ่มแกนเพื่อให้มี batch size เป็น 1
    return image

# หัวข้อเว็บ
st.title("Image Classification with TensorFlow")

# อัปโหลดไฟล์โมเดล
model_file = st.file_uploader("Upload your Keras model (.h5)", type=["h5"])

if model_file:
    # โหลดโมเดล
    model = load_model(model_file)
    st.success("Model loaded successfully!")

    # อัปโหลดไฟล์รูปภาพ
    image_file = st.file_uploader("Upload an image for prediction", type=["jpg", "jpeg", "png"])

    if image_file:
        # แสดงภาพที่อัปโหลด
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # เตรียมข้อมูลสำหรับการทำนาย
        input_image = preprocess_image(image, target_size=(224, 224))  # เปลี่ยนขนาดภาพตามโมเดลของคุณ

        # ประมวลผลการทำนาย
        prediction = model.predict(input_image)

        # แสดงผลลัพธ์การทำนาย
        st.write("Prediction:", prediction)
        st.write("Predicted class:", np.argmax(prediction))
