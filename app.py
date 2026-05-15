import streamlit as st
from paddleocr import PaddleOCR
from PIL import Image
import tempfile

st.set_page_config(
    page_title="Vietnamese Document Intelligence",
    layout="wide"
)

st.title("📄 Vietnamese Document Intelligence Platform")

@st.cache_resource
def load_ocr():
    return PaddleOCR(
        use_textline_orientation=True,
        lang='en',
        ocr_version='PP-OCRv4'
    )

ocr = load_ocr()

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:

        image.save(tmp.name)

        result = ocr.ocr(tmp.name)

    extracted_text = []

    try:
        for line in result:
            for word in line:
                extracted_text.append(word[1][0])

    except:
        extracted_text.append("OCR parsing error")

    final_text = "\n".join(extracted_text)

    st.subheader("OCR Result")

    st.text_area(
        "Extracted Text",
        final_text,
        height=300
    )