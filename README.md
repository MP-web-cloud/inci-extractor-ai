# Outil d'extraction INCI IA

## Installation

1. Créer un environnement virtuel :
```
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
```

2. Installer les dépendances :
```
pip install -r requirements.txt
```

3. Renommer `.env.example` en `.env` et ajouter votre clé OpenAI :
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

4. Lancer l'application :
```
streamlit run app.py
```

## Fonctionnalités

- Dépôt PDF/image
- Extraction texte
- Extraction automatique INCI via LLM
- Mise à jour automatique de la base
- Export CSV
