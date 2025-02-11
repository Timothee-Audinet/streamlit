import streamlit as st


def show_home():
    st.container():
    st.markdown("""
        <div class="header-container">
            <img src="https://raw.githubusercontent.com/Timothee-Audinet/streamlit/refs/heads/main/ImageProfile.png" alt="Bannière">
            <div class="header-text"><h1>Timothée Audinet</h1><h2>Photographe Animalier</h2></div>
        </div>
        """, unsafe_allow_html=True)
    st.write(
        "Passionné par la photographie animalière, je capture la beauté de la faune sauvage dans son habitat naturel. "
        "À travers mes clichés, j'espère sensibiliser à la préservation des espèces et partager des moments uniques avec la nature."
    )
