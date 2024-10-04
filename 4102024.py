import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

st.title("Webcam Stream")

# ตรวจสอบการตั้งค่า RTC
rtc_configuration = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

# เรียกใช้งาน webrtc_streamer พร้อม RTC configuration
webrtc_streamer(
    key="example",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=rtc_configuration
)