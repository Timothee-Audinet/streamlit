import streamlit as st


def show_galerie():
    st.title("📷 Galerie de Photographie")
    cols = st.columns(3)
  
    for i, filename in enumerate(photo_files):
        img_url = photo_dir + filename  # URL complète de l'image
        with cols[i % 3]:
            st.image(img_url, use_container_width=True)
            st.caption(filename.split(".")[0])  # Affiche le nom du fichier
