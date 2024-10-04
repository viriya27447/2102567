import streamlit as st
from jupyter_code import calculate_sum  # import ฟังก์ชันจาก Jupyter

# Streamlit UI
st.title('Jupyter + Streamlit Integration')
a = st.number_input('Enter a number', value=0)
b = st.number_input('Enter another number', value=0)

if st.button('Calculate'):
    result = calculate_sum(a, b)
    st.write(f'The result is {result}')
