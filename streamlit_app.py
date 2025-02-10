import streamlit as st
from PIL import Image
import os

# Configuration de la page
st.set_page_config(page_title="Wildlife Photography Portfolio", layout="wide")

# Sidebar (profil personnel)
st.sidebar.image("https://raw.githubusercontent.com/Timothee-Audinet/streamlit/refs/heads/main/LES%20JOURETS_08%202024-0718.jpg", width=150)
st.sidebar.markdown("## À propos de moi")
st.sidebar.write("Passionné de photographie animalière, j'aime capturer la beauté de la nature.")
st.sidebar.markdown("[Mon Instagram](https://www.instagram.com/timothee_wildlife_photo/)")

# Menu horizontal
menu = st.selectbox("Navigation", ["Photographie", "Wallpapers"])

# Dossier contenant les images (à adapter)
photo_dir = "photos"
wallpaper_dir = "wallpapers"

if menu == "Photographie":
    st.title("📷 Galerie de Photographie")
    cols = st.columns(3)
    
    for i, filename in enumerate(os.listdir(photo_dir)):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(photo_dir, filename)
            img = Image.open(img_path)
            with cols[i % 3]:
                st.image(img, use_column_width=True)
                st.caption(f"{filename.split('.')[0]}")  # Nom de l'image comme légende

elif menu == "Wallpapers":
    st.title("🖼️ Téléchargez un Wallpaper")
    cols = st.columns(3)
    
    for i, filename in enumerate(os.listdir(wallpaper_dir)):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(wallpaper_dir, filename)
            img = Image.open(img_path)
            with cols[i % 3]:
                st.image(img, use_column_width=True)
                st.download_button("Télécharger", img_path, file_name=filename)


