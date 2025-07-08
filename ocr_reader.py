import pytesseract
from pdf2image import convert_from_path
import os

def ocr_pdf(pdf_path):
    try:
        # Convert PDF to list of PIL images
        images = convert_from_path(pdf_path)

        full_text = ""
        for page_num, img in enumerate(images):
            text = pytesseract.image_to_string(img)
            full_text += f"\n\n--- Page {page_num + 1} ---\n{text}"

        return full_text.strip()
    except Exception as e:
        return f"Error during OCR: {str(e)}"
