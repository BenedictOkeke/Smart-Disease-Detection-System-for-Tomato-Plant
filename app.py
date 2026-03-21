import streamlit as st

st.title("Tomato Disease Detection")

uploaded_file = st.file_uploader("Upload a tomato leaf image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("Prediction will appear here...")