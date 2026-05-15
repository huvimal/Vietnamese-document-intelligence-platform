import streamlit as st
import requests

st.set_page_config(
    page_title="Vietnamese Document Intelligence",
    layout="wide"
)

st.title("📄 Vietnamese Document Intelligence Platform")

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue()
        )
    }

    response = requests.post(
        "http://127.0.0.1:8080/documents/upload",
        files=files
    )

    if response.status_code == 200:

        st.success("Upload successful!")

        st.json(response.json())

    else:
        st.error("Upload failed")