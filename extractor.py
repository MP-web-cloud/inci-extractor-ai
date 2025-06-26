import pdfplumber
import pytesseract
from PIL import Image
import requests

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_image(image_file):
    image = Image.open(image_file)
    return pytesseract.image_to_string(image)

def extract_inci_from_text(text):
    prompt = (
        "Voici un texte fournisseur. Liste uniquement les noms INCI ou noms chimiques, séparés par des virgules:\n\n" +
        text
    )
    resp = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    data = resp.json()
    return [inci.strip() for inci in data["response"].split(",") if inci.strip()]
