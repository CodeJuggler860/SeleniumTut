import pdfplumber
import pytesseract
from PIL import Image
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    else:  # image
        img = Image.open(file_path)
        return pytesseract.image_to_string(img)
