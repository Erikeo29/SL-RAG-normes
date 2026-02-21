"""Pages de contenu normatif (medical et statistique)."""
import streamlit as st

from utils.data_loaders import load_file_content


def render_normes_medical_page():
    """Affiche la page de synthese des normes medicales."""
    st.session_state.domain = "medical"
    content = load_file_content("medical/medical_overview.md")
    st.markdown(content, unsafe_allow_html=True)


def render_normes_statistique_page():
    """Affiche la page de synthese des normes statistiques."""
    st.session_state.domain = "statistique"
    content = load_file_content("statistique/statistique_overview.md")
    st.markdown(content, unsafe_allow_html=True)
