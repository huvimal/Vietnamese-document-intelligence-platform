import streamlit as st
from paddleocr import PaddleOCR
from PIL import Image
import tempfile

# Sửa lỗi ngoặc kép ở đây
st.set_page_config(
    page_title="Vietnamese Document Intelligence",
    layout="wide"
)

st.title("📄 Vietnamese Document Intelligence Platform")

ocr = PaddleOCR(
    use_angle_cls=True,
    lang='vi'
)

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        image.save(tmp.name)
        # PaddleOCR trả về danh sách, cần xử lý cẩn thận
        result = ocr.ocr(tmp.name)

    extracted_text = []
    
    # Kiểm tra kết quả ocr trước khi lặp
    if result and result[0]:
        for line in result:
            for word in line:
                extracted_text.append(word[1][0])

    final_text = "\n".join(extracted_text)

    st.subheader("OCR Result")
    st.text_area(
        "Extracted Text",
        final_text,
        height=300
    )