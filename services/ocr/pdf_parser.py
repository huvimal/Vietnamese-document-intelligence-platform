import fitz
from PIL import Image
import os


def pdf_to_images(pdf_path, output_dir="temp_pages"):

    os.makedirs(output_dir, exist_ok=True)

    pdf_document = fitz.open(pdf_path)
    image_paths = []

    for page_number in range(len(pdf_document)):

        page = pdf_document.load_page(page_number)
        pix = page.get_pixmap()

        image_path = f"{output_dir}/page_{page_number}.png"
        pix.save(image_path)

        image_paths.append(image_path)

    return image_paths