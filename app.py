import streamlit as st
from extractor import extract_text_from_pdf, extract_text_from_image, extract_inci_from_text
from utils import load_inci_base, update_inci_base
import pandas as pd

st.title("Extracteur INCI IA")
st.write("Déposez un fichier PDF ou image pour extraire automatiquement les INCI/noms chimiques.")

uploaded_file = st.file_uploader("Choisissez un fichier PDF ou image", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = extract_text_from_image(uploaded_file)

    st.subheader("Texte extrait")
    st.text_area("Contenu du document :", text, height=200)

    with st.spinner("Extraction des INCI en cours..."):
        incis = extract_inci_from_text(text)

    st.subheader("INCI détectés")
    st.write(incis)

    new_incis = update_inci_base(incis)

    st.success(f"{len(new_incis)} nouveaux INCI ajoutés à la base locale.")

    st.download_button("Télécharger les INCI extraits", pd.DataFrame({"INCI": incis}).to_csv(index=False), "incis_extraits.csv")
    st.download_button("Télécharger la base INCI complète", load_inci_base().to_csv(index=False), "base_inci.csv")
