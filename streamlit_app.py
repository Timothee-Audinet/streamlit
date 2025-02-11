import streamlit as st
from streamlit_option_menu import option_menu
from st_social_media_links import SocialMediaIcons

# Configuration de la page
st.set_page_config(layout="wide")


social_media_links1 = [
    "https://www.instagram.com/timothee_wildlife_photo/",
]
social_media_links2 = [
    "https://github.com/Timothee-Audinet",
]

### POLICE ###
with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 5rem;
            padding-right: 5rem;
        }
        /* Menu de navigation */
        .css-18e3th9 {
            background-color: #333 !important;
            padding: 200px 0 !important;
            width: 100% !important;
            display: flex;
            justify-content: center;
        }
        .css-18e3th9 span {
            font-size: 24px !important;
            font-weight: bold;
            letter-spacing: 1.5px;
            color: #ddd !important;
        }
         .st-emotion-cache-1jicfl2 {
            width: 100%;
            padding: 6rem 1rem 10rem;
            min-width: auto;
            max-width: initial;
        }
        /* Police globale */
        * {
            font-family: 'Didact Gothic', sans-serif !important;
        }
        /* En-tête */
        .header-container {
            position: relative;
            text-align: center;
            color: white;
            width: 100%;
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
            width: 80%; /* Largeur du texte max pour éviter qu’il devienne trop large */
        }
        .header-text h1 {
            font-size: 4vw; /* 6% de la largeur de l'écran */
            font-weight: bold;
            margin: 0;
        }
        .header-text h2 {
            font-size: 2vw; /* 3% de la largeur de l'écran */
            font-weight: normal;
        }
        /* Section contenu limité */
        .content-container {
            width: 50%;
            margin: auto;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .wallpaper-image {
            width: 60%; /* Modifier ce pourcentage selon la taille désirée */
            height: auto;
            display: block;
            margin: auto;
        }
        .download-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True
)



# Définir les liens GitHub des dossiers d'images
GITHUB_USERNAME = "Timothee-Audinet"
REPO_NAME = "streamlit"
BRANCH = "main"
wallpaper_dir = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/{BRANCH}/wallpaper_dir/"
## Liste des images (à adapter selon ton repo)
wallpaper_files = ["12.png","18.png","21.png","24.png","26.png","29.png"]  # Idem ici

st.title("🖼️ Fonds d'écran")
st.markdown("<div class='content-container'>", unsafe_allow_html=True)
st.header("N'hésitez pas à télécharger !", divider=True)    
st.write(
    "Pour me remercier vous pouvez partager votre nouveau fond d'écran en m'identifiant sur votre story, me suivre, partager certaines de mes photos."
)
st.write("Merci.")
st.header(" ", divider=True)    

cols = st.columns(3)
for i, filename in enumerate(wallpaper_files):
    img_url = wallpaper_dir + filename
    with cols[i % 3]:
      st.markdown(f"""<div class="download-container"> <img src="{img_url}" class="wallpaper-image"> <br> <a href="{img_url}" download="{filename}"> <button style="padding: 10px 20px; font-size: 16px;">Télécharger</button> </a></div>""", unsafe_allow_html=True)
