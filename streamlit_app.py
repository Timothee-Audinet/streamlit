import streamlit as st
from streamlit_option_menu import option_menu

# Configuration de la page
st.set_page_config(layout="wide")


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
        "Vous trouverez plusieurs onglets, avec une galerie photos et les fonds d'écrans téléchargeables. Le site est encore en cours de construction (je l'écris tout seul)."
    )
    st.markdown("### A propos")
    st.write(    
        "Je suis actuellement en thèse de chimie quantique où j'étudie l'infuence des propriétés relativistes sur la structure des atomes."
        "Mais de puis tout petit, je suis passionné par la photographie animalière. Il y a 4 ans j'ai commencé à photographier les animaux que j'aimais observer."
        "J'essaye de capturer la beauté de la faune sauvage dans son habitat naturel. "
        "À travers mes clichés, j'espère sensibiliser à la préservation des espèces et partager des moments uniques avec la nature."
        "N'hésitez pas à me suivre sur instagram pour recommander mon travail, cela aide beaucoup !"
    )
    st.markdown("</div>", unsafe_allow_html=True)

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
