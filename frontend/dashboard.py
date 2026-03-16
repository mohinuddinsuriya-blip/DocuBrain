import streamlit as st
import requests
import plotly.express as px

st.title("Document Intelligence Platform")

file = st.file_uploader("Upload Document")

if file:

    response = requests.post(
        "http://127.0.0.1:8000/upload",
        files={"file": file}
    )

    data = response.json()

    st.write("Stakeholders:", data["stakeholders"])

    st.write("Timeline:", data["timeline"])