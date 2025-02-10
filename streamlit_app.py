#import streamlit as st
#from streamlit_option_menu import option_menu
##from PIL import Image
##import os
#
## Configuration de la page
#st.set_page_config(page_title="Wildlife Photography Portfolio", layout="wide")
#
## Sidebar (profil personnel)
#st.sidebar.image("https://raw.githubusercontent.com/Timothee-Audinet/streamlit/refs/heads/main/LES%20JOURETS_08%202024-0718.jpg", width=250)
#st.sidebar.markdown("## À propos de moi")
#st.sidebar.write("Passionné de photographie animalière, j'aime capturer la beauté de la nature.")
#st.sidebar.markdown("[Mon Instagram](https://www.instagram.com/timothee_wildlife_photo/)")
#
## Menu horizontal
#
##menu = st.selectbox("Navigation", ["Photographie", "Wallpapers"], key="menu_navigation")
#selected = option_menu(
#    menu_title=None,  # Pas de titre principal
#    options=["ACCUEIL", "PHOTOGRAPHIE", "WALLPAPERS"],
#    icons=["house", "camera", "image"],
#    menu_icon="cast",
#    default_index=0,
#    orientation="horizontal",
#    styles={
#        "container": {"padding": "0px", "background-color": "#333"},
#        "icon": {"color": "#bbb", "font-size": "18px"},
#        "nav-link": {"color": "#bbb", "font-size": "16px", "text-align": "center", "padding": "10px"},
#        "nav-link-selected": {"color": "white", "font-weight": "bold", "border-bottom": "2px solid white"},
#    }
#)


# Définir les liens GitHub des dossiers d'images
#GITHUB_USERNAME = "Timothee-Audinet"
#REPO_NAME = "streamlit"
#BRANCH = "main"
#photo_dir = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/refs/heads/main/photos_dir/"
#wallpaper_dir = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/refs/heads/main/wallpaper_dir/"
## Liste des images (à adapter selon ton repo)
#photo_files = ["BROCARDweb-4994.jpg", "MOYENDUC-1434-3.jpg", "OURSweb-6686-3.jpg"]  # Remplace par tes fichiers réels
#wallpaper_files = ["FondEcran-Gobemouche-3556.jpg"]  # Idem ici
#
#if selected == "ACCUEIL":
#    st.title("🏠 Bienvenue sur la page d'accueil")
#elif selected == "PHOTOGRAPHIE":
#    st.title("📷 Galerie de Photographie")
#    cols = st.columns(3)
#    
#    for i, filename in enumerate(photo_files):
#        img_url = photo_dir + filename  # URL complète de l'image
#        with cols[i % 3]:
#            st.image(img_url, use_container_width=True)
#            st.caption(filename.split(".")[0])  # Affiche le nom du fichier
#
#elif selected == "WALLPAPERS":
#    st.title("🖼️ Téléchargez un Wallpaper")
#    cols = st.columns(3)
#    
#    for i, filename in enumerate(wallpaper_files):
#        img_url = wallpaper_dir + filename
#        with cols[i % 3]:
#            st.image(img_url, use_container_width=True)
#            st.download_button("Télécharger", img_url, file_name=filename)

import streamlit as st
from streamlit_option_menu import option_menu

# Configuration de la page
st.set_page_config(layout="wide")

# Style CSS personnalisé
st.markdown(
    """
    <style>
        /* Menu de navigation */
        .css-18e3th9 {
            background-color: #333 !important;
            padding: 30px 0 !important;
        }
        .css-18e3th9 span {
            font-size: 24px !important;
            font-weight: bold;
            letter-spacing: 1.5px;
            color: #ddd !important;
        }
        /* En-tête */
        .header-container {
            position: relative;
            text-align: center;
            color: white;
        }
        .header-container img {
            width: 100%;
            height: auto;
            filter: brightness(60%);
        }
        .header-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
        }
        .header-text h1 {
            font-size: 80px;
            font-weight: bold;
            margin: 0;
        }
        .header-text h2 {
            font-size: 40px;
            font-weight: normal;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Barre de navigation
selected = option_menu(
    menu_title=None,
    options=["ACCUEIL", "BIOGRAPHIE", "GALERIE ARTISTIQUE", "FORMATIONS", "MATERIELS", "BOUTIQUE", "CONTACTS"],
    icons=["house", "person", "image", "book", "tools", "cart", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Section Accueil
st.markdown('<div class="header-container">', unsafe_allow_html=True)
st.image("header.jpg", use_column_width=True)
st.markdown(
    '<div class="header-text"><h1>Prénom Nom</h1><h2>Photographe Animalier</h2></div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# --- Menu en pleine largeur ---
#with st.container():
#    selected = option_menu(
#        menu_title=None,
#        options=["Accueil", "Galerie", "Fond d'écran", "Contact"],
#        icons=["house", "image", "info-circle", "envelope"],
#        menu_icon="cast",
#        default_index=0,
#        orientation="horizontal",
#        styles={
#            "container": {"padding": "0!important", "background-color": "#333"},
#            "icon": {"color": "white", "font-size": "18px"},
#            "nav-link": {"font-size": "18px", "color": "white", "text-align": "center", "margin": "0px"},
#            "nav-link-selected": {"background-color": "#555"},
#        }
#    )

# Définir les liens GitHub des dossiers d'images
GITHUB_USERNAME = "Timothee-Audinet"
REPO_NAME = "streamlit"
BRANCH = "main"
photo_dir = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/refs/heads/main/photos_dir/"
wallpaper_dir = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/refs/heads/main/wallpaper_dir/"
## Liste des images (à adapter selon ton repo)
photo_files = ["BROCARDweb-4994.jpg", "MOYENDUC-1434-3.jpg", "OURSweb-6686-3.jpg"]  # Remplace par tes fichiers réels
wallpaper_files = ["FondEcran-Gobemouche-3556.jpg"]  # Idem ici

# --- Page d'Accueil ---
#if selected == "Accueil":
#    with st.container():
#        st.markdown("""
#        <div class="header-container">
#            <img src="https://raw.githubusercontent.com/Timothee-Audinet/streamlit/refs/heads/main/LES%20JOURETS_08%202024-0718.jpg" alt="Bannière">
#            <div class="header-text">Prénom Nom<br>Photographe Animalier</div>
#        </div>
#        """, unsafe_allow_html=True)
#    
#    st.markdown("### 📖 À Propos")
#    st.write(
#        "Passionné par la photographie animalière, je capture la beauté de la faune sauvage dans son habitat naturel. "
#        "À travers mes clichés, j'espère sensibiliser à la préservation des espèces et partager des moments uniques avec la nature."
#    )

# --- Portfolios ---
if selected == "Galerie":
    st.title("📷 Galerie de Photographie")
    cols = st.columns(3)
    
    for i, filename in enumerate(photo_files):
        img_url = photo_dir + filename  # URL complète de l'image
        with cols[i % 3]:
            st.image(img_url, use_container_width=True)
            st.caption(filename.split(".")[0])  # Affiche le nom du fichier

if selected == "Fond d'écran":
    st.title("🖼️ Téléchargez un Wallpaper")
    cols = st.columns(3)
    
    for i, filename in enumerate(wallpaper_files):
        img_url = wallpaper_dir + filename
        with cols[i % 3]:
            st.image(img_url, use_container_width=True)
            st.download_button("Télécharger", img_url, file_name=filename)

# --- Page Contact ---
if selected == "Contact":
    st.markdown("## 📩 Contact")
    st.write("Formulaire de contact ou infos ici...")
