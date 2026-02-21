"""RAG documents reglementaires — Point d'entree Streamlit."""
import streamlit as st

from config import CSS_PATH
from components.sidebar import render_sidebar
from components.chat_page import render_chat_page
from components.upload_page import render_upload_page
from components.matrix_page import render_matrix_page
from components.about_page import render_about_page
from utils.translations import t


# --- Page config ---
st.set_page_config(
    page_title="RAG Normes",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Session state init ---
if "lang" not in st.session_state:
    st.session_state.lang = "fr"
if "current_page" not in st.session_state:
    st.session_state.current_page = "chat"
if "domain" not in st.session_state:
    st.session_state.domain = "medical"

# Per-domain chat histories
for _dom in ("medical", "statistique"):
    if f"chat_messages_{_dom}" not in st.session_state:
        st.session_state[f"chat_messages_{_dom}"] = []
    if f"chat_sources_{_dom}" not in st.session_state:
        st.session_state[f"chat_sources_{_dom}"] = []

# Migration: ancien chat_messages mono-domaine → medical
if "chat_messages" in st.session_state and st.session_state.chat_messages:
    st.session_state.chat_messages_medical = st.session_state.chat_messages
    st.session_state.chat_sources_medical = st.session_state.get("chat_sources", [])
    del st.session_state["chat_messages"]
    del st.session_state["chat_sources"]
elif "chat_messages" in st.session_state:
    del st.session_state["chat_messages"]
    if "chat_sources" in st.session_state:
        del st.session_state["chat_sources"]


# --- CSS ---
@st.cache_data(ttl=3600)
def load_css(path: str) -> str:
    with open(path) as f:
        return f.read()


try:
    css = load_css(CSS_PATH)
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass


# --- Sidebar ---
render_sidebar()


# --- Routing ---
page = st.session_state.current_page

if page == "chat":
    render_chat_page()
elif page == "upload":
    render_upload_page()
elif page == "matrix":
    render_matrix_page()
elif page == "about":
    render_about_page()
