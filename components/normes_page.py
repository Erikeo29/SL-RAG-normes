"""Pages de contenu normatif (medical et statistique)."""
import os
import re

import streamlit as st

from config import ASSETS_PATH
from utils.data_loaders import load_file_content


def _render_markdown_with_images(content: str, image_dir: str):
    """Rendu markdown avec support des marqueurs <!-- IMG:filename.png -->.

    Les images sont chargees depuis image_dir via st.image().
    Les portions de texte entre les marqueurs sont rendues via st.markdown().
    """
    parts = re.split(r"<!-- IMG:(\S+?) -->", content)
    for i, part in enumerate(parts):
        if i % 2 == 0:
            # Texte markdown
            text = part.strip()
            if text:
                st.markdown(text, unsafe_allow_html=True)
        else:
            # Nom de fichier image
            img_path = os.path.join(image_dir, part)
            if os.path.exists(img_path):
                st.image(img_path)


def render_normes_medical_page():
    """Affiche la page de synthese des normes medicales."""
    st.session_state.domain = "medical"
    content = load_file_content("medical/medical_overview.md")
    image_dir = os.path.join(ASSETS_PATH, "images", "medical")
    _render_markdown_with_images(content, image_dir)


def render_normes_statistique_page():
    """Affiche la page de synthese des normes statistiques."""
    st.session_state.domain = "statistique"
    content = load_file_content("statistique/statistique_overview.md")
    image_dir = os.path.join(ASSETS_PATH, "images", "statistique")
    _render_markdown_with_images(content, image_dir)
