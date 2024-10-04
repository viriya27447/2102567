import streamlit as st
from streamlit_webrtc import webrtc_streamer

# ตั้งชื่อให้กับแอป
st.title("Webcam Stream")

# เรียกใช้งาน webrtc_streamer
webrtc_streamer(key="example")
