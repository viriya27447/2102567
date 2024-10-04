import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("Webcam Live Stream")
webrtc_streamer(key="example")
