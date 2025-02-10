import streamlit as st
#from PIL import Image
#import os

# Configuration de la page
st.set_page_config(page_title="Wildlife Photography Portfolio", layout="wide")

# Sidebar (profil personnel)
st.sidebar.image("https://raw.githubusercontent.com/Timothee-Audinet/streamlit/refs/heads/main/LES%20JOURETS_08%202024-0718.jpg", width=250)
st.sidebar.markdown("## À propos de moi")
st.sidebar.write("Passionné de photographie animalière, j'aime capturer la beauté de la nature.")
st.sidebar.markdown("[Mon Instagram](https://www.instagram.com/timothee_wildlife_photo/)")

# Menu horizontal
menu = st.selectbox("Navigation", ["Photographie", "Wallpapers"])

# Définir les liens GitHub des dossiers d'images
GITHUB_USERNAME = "Timothee_Audinet"
REPO_NAME = "streamlit"
BRANCH = "main"

photo_dir = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/refs/heads/main/photos_dir/"
wallpaper_dir = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/refs/heads/main/wallpaper_dir/"

# Liste des images (à adapter selon ton repo)
photo_files = ["BROCARDweb-4994.jpg", "MOYENDUC-1434-3.jpg", "OURSweb-6686-3.jpg"]  # Remplace par tes fichiers réels
wallpaper_files = ["FondEcran-Gobemouche-3556.jpg"]  # Idem ici

menu = st.selectbox("Navigation", ["Photographie", "Wallpapers"])

if menu == "Photographie":
    st.title("📷 Galerie de Photographie")
    cols = st.columns(3)
    
    for i, filename in enumerate(photo_files):
        img_url = photo_dir + filename  # URL complète de l'image
        with cols[i % 3]:
            st.image(img_url, use_column_width=True)
            st.caption(filename.split(".")[0])  # Affiche le nom du fichier

elif menu == "Wallpapers":
    st.title("🖼️ Téléchargez un Wallpaper")
    cols = st.columns(3)
    
    for i, filename in enumerate(wallpaper_files):
        img_url = wallpaper_dir + filename
        with cols[i % 3]:
            st.image(img_url, use_column_width=True)
            st.download_button("Télécharger", img_url, file_name=filename)

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


