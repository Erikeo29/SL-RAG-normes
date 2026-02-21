"""Composant sidebar : navigation, domaine, langue, stats base."""
import streamlit as st

from config import DOMAINS, VERSION, VERSION_DATE
from core.ingestion import get_db_stats
from utils.translations import t


def render_sidebar():
    """Affiche le sidebar avec navigation et informations."""
    with st.sidebar:
        st.title(t("app_title"))

        st.markdown("---")

        # Domaine
        domain_keys = list(DOMAINS.keys())
        domain_labels = [
            f"{DOMAINS[d]['icon']} {t(f'domain_{d}')}" for d in domain_keys
        ]
        current_domain = st.session_state.get("domain", "medical")
        domain_idx = (
            domain_keys.index(current_domain)
            if current_domain in domain_keys
            else 0
        )
        selected_domain = st.radio(
            t("domain_label"),
            options=domain_labels,
            index=domain_idx,
            horizontal=True,
            key="domain_radio",
        )
        new_domain = domain_keys[domain_labels.index(selected_domain)]
        if new_domain != current_domain:
            st.session_state.domain = new_domain
            st.rerun()

        st.markdown("---")

        # Langue
        lang_options = {"Francais": "fr", "English": "en"}
        current_lang = st.session_state.get("lang", "fr")
        default_idx = 0 if current_lang == "fr" else 1
        selected = st.radio(
            t("lang_label"),
            options=list(lang_options.keys()),
            index=default_idx,
            horizontal=True,
            key="lang_radio",
        )
        new_lang = lang_options[selected]
        if new_lang != current_lang:
            st.session_state.lang = new_lang
            st.rerun()

        st.markdown("---")

        # Navigation
        st.subheader(t("sidebar_title"))
        page_keys = ["chat", "upload", "matrix", "about"]
        page_labels = [
            t("page_chat"),
            t("page_upload"),
            t("page_matrix"),
            t("page_about"),
        ]
        current = st.session_state.get("current_page", "chat")
        nav_idx = page_keys.index(current) if current in page_keys else 0
        selected_page = st.radio(
            "Page",
            options=page_labels,
            index=nav_idx,
            label_visibility="collapsed",
            key="nav_radio",
        )
        st.session_state.current_page = page_keys[page_labels.index(selected_page)]

        st.markdown("---")

        # Stats base — domaine actif
        collection_name = DOMAINS[new_domain]["collection"]
        stats = get_db_stats(collection_name=collection_name)
        domain_label = t(f"domain_{new_domain}")
        st.subheader(f"{t('db_stats_title')} — {domain_label}")
        col1, col2 = st.columns(2)
        col1.metric(t("db_docs"), stats["documents"])
        col2.metric(t("db_chunks"), stats["chunks"])

        if stats["sources"]:
            with st.expander(t("db_indexed_docs")):
                for src in stats["sources"]:
                    st.caption(f"- {src}")

        st.markdown("---")
        st.caption(f"{t('version_label')} {VERSION} ({VERSION_DATE})")
        st.caption("MIT License")
