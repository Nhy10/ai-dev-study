import streamlit as st

st.title("GDG KU 파이팅")

user_input = st.text_input("Enter the name", "Guest")

if st.button("Say GOOD"):
    st.write(f"Hello, {user_input}")

slider_value = st.slider("Pick_number", 0, 100)
st.write(f"slider_value, {slider_value}")

if st.checkbox("checkbox"):
    st.write("checkout!")