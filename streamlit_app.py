import streamlit as st
from streamlit_option_menu import option_menu
from st_social_media_links import SocialMediaIcons

# Configuration de la page
st.set_page_config(layout="wide")


social_media_links = [
    "https://www.instagram.com/timothee_wildlife_photo/",
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


# --- Menu en pleine largeur ---
#with st.container():
#    selected = option_menu(
#        menu_title=None,
#        options=["Accueil", "Galerie", "Fond d'écran", "Contact"],
#        icons=["house", "image", "phone", "envelope"],
#        menu_icon="cast",
#        default_index=0,
#        orientation="horizontal",
#        styles={
#            "container": {"padding": "0!important", "background-color": "#333", "width": "100%", "display": "flex", "justify-content": "center"},
#            "icon": {"color": "white", "font-size": "18px"},
#            "nav-link": {"font-size": "18px", "color": "white", "text-align": "center", "margin": "0px"},
#            "nav-link-selected": {"background-color": "#555"},
#        }
#    )

with st.sidebar:
    selected = st.radio(
        "Navigation", 
        ["Accueil", "Galerie", "Fond d'écran", "Contact"]
    )
    social_media_icons = SocialMediaIcons(social_media_links)
    social_media_icons.render()

# Définir les liens GitHub des dossiers d'images
GITHUB_USERNAME = "Timothee-Audinet"
REPO_NAME = "streamlit"
BRANCH = "main"
photo_dir = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/{BRANCH}/photos_dir/"
wallpaper_dir = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/{BRANCH}/wallpaper_dir/"
## Liste des images (à adapter selon ton repo)
photo_files = ["Hibou Moyen-Duc.jpg","Lynx Ibérique.png","Daim.png","Troglodyte Mignon.png","Chevrette.png","Brocard.jpg","Daim au coucher de soleil.png","Grand Tétras.png","Huîtrier Pie.png","Lever de soleil.png","Lynx Pardelle.png","Ours Brun.jpg","Sanglier.jpg"]  # Remplace par tes fichiers réels
wallpaper_files = ["12.png","18.png","21.png","24.png","26.png","29.png"]  # Idem ici

# --- Page d'Accueil ---
if selected == "Accueil":
    with st.container():
        st.markdown("""
        <div class="header-container">
            <img src="https://raw.githubusercontent.com/Timothee-Audinet/streamlit/refs/heads/main/ImageProfile.png" alt="Bannière">
            <div class="header-text"><h1>Timothée Audinet</h1><h2>Photographe Animalier</h2></div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div class='content-container'>", unsafe_allow_html=True)
    st.markdown("### Bienvenue")
    st.write(
        "Bienvenue sur mon site de photographie animalière."
    )
    st.write(
        "Vous trouverez plusieurs onglets, avec une galerie photos et les fonds d'écrans téléchargeables."
    )
    st.write(
        "Le site est encore en cours de construction, j'apprend petit à petit."
    )
    st.markdown("### A propos")
    st.write(    
        "Je suis actuellement en thèse de chimie quantique où j'étudie l'infuence des propriétés relativistes sur la structure des atomes."
    )
    st.write(
        "Mais depuis l'enfance, je suis passionné par la faune sauvage. Il y a 4 ans j'ai commencé à photographier les animaux que j'aimais observer."
    )
    st.write(
        "J'essaye de capturer la beauté de la faune sauvage dans son habitat naturel, sans causer le moindre dérangement. "
        "L'utilisation d'appât ou autres moyens d'approcher les animaux ne représente pas pour moi l'éthique photographique. "
        "Seule l'attente et la patience me permettent d'obtenir mes photos."
    )
    st.write(
        "À travers mes clichés, j'espère sensibiliser à la préservation des espèces et partager des moments uniques avec la nature."
    )
    st.write(
        "N'hésitez pas à me suivre sur instagram pour recommander mon travail, cela aide beaucoup !"
    )
    st.markdown("</div>", unsafe_allow_html=True)

    social_media_icons = SocialMediaIcons(social_media_links)
    social_media_icons.render()

# --- Portfolios ---
if selected == "Galerie":
    st.title("📷 Galerie Photo")
    cols = st.columns(3)
    
    for i, filename in enumerate(photo_files):
        img_url = photo_dir + filename  # URL complète de l'image
        with cols[i % 3]:
            st.image(img_url, use_container_width=True)
            st.caption(filename.split(".")[0])  # Affiche le nom du fichier

if selected == "Fond d'écran":
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

            
    #st.markdown(f'<img src="{img_url}" class="wallpaper-image">', unsafe_allow_html=True)
    #st.download_button("Télécharger", img_url, file_name=filename)
    
    #for i, filename in enumerate(wallpaper_files):
    #    img_url = wallpaper_dir + filename
    #    with cols[i % 3]:
    #        st.image(img_url, use_container_width=True)
    #        st.download_button("Télécharger", img_url, file_name=filename)

# --- Page Contact ---
if selected == "Contact":
    st.markdown("## 📩 Contact")
    st.write("Formulaire de contact ou infos ici...")
