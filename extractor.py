import pdfplumber
import pytesseract
from PIL import Image
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_image(image_file):
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)
    return text

def extract_inci_from_text(text):
    prompt = (
        "Voici le contenu d’un document fournisseur. "
        "Extrais tous les noms INCI ou les noms chimiques des matières premières présentes dans ce texte. "
        "Liste uniquement les noms, séparés par des virgules."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt + "\n\n" + text}
        ]
    )
    content = response.choices[0].message.content
    return [inci.strip() for inci in content.split(",") if inci.strip()]
