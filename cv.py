import streamlit as st
from PIL import Image

# Titre de l'application
st.title("CV Electronique")

# Affichage des informations personnelles
st.header("Informations Personnelles")
name = st.text_input("Nom complet", "")
email = st.text_input("Adresse email", "")
...

# Affichage de la photo de profil
st.header("Photo de Profil")
profile_image = Image.open("images\portrait_hermann.jpg")
st.image(profile_image, caption="Votre photo de profil", use_column_width=True)
