"""Composant sidebar : langue, navigation groupée par domaine, stats, annexes."""
import streamlit as st

from config import DOMAINS
from core.ingestion import get_db_stats
from utils.translations import t


def render_sidebar():
    """Affiche le sidebar avec navigation et informations."""
    with st.sidebar:
        st.title(t("app_title"))

        st.markdown("---")

        # Langue (tout en haut)
        lang_options = {"Français": "fr", "English": "en"}
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

        # Navigation par boutons groupés
        current = st.session_state.get("current_page", "about")
        domain = st.session_state.get("domain", "medical")

        # À propos
        if st.button(
            t("page_about"),
            type="primary" if current == "about" else "secondary",
            use_container_width=True,
            key="btn_about",
        ):
            st.session_state.current_page = "about"
            st.rerun()

        st.markdown("---")

        # --- Médical ---
        st.caption(t("section_medical"))

        if st.button(
            t("page_normes_medical"),
            type="primary" if current == "normes_medical" else "secondary",
            use_container_width=True,
            key="btn_normes_medical",
        ):
            st.session_state.current_page = "normes_medical"
            st.session_state.domain = "medical"
            st.rerun()

        if st.button(
            t("page_chat_medical"),
            type=(
                "primary"
                if current == "chat" and domain == "medical"
                else "secondary"
            ),
            use_container_width=True,
            key="btn_chat_medical",
        ):
            st.session_state.current_page = "chat"
            st.session_state.domain = "medical"
            st.rerun()

        st.markdown("---")

        # --- Statistique ---
        st.caption(t("section_statistique"))

        if st.button(
            t("page_normes_statistique"),
            type="primary" if current == "normes_statistique" else "secondary",
            use_container_width=True,
            key="btn_normes_statistique",
        ):
            st.session_state.current_page = "normes_statistique"
            st.session_state.domain = "statistique"
            st.rerun()

        if st.button(
            t("page_chat_statistique"),
            type=(
                "primary"
                if current == "chat" and domain == "statistique"
                else "secondary"
            ),
            use_container_width=True,
            key="btn_chat_statistique",
        ):
            st.session_state.current_page = "chat"
            st.session_state.domain = "statistique"
            st.rerun()

        st.markdown("---")

        # Stats base (compact, les deux domaines)
        all_stats = {}
        for dom, cfg in DOMAINS.items():
            all_stats[dom] = get_db_stats(collection_name=cfg["collection"])

        st.caption(t("db_stats_title"))
        for dom in DOMAINS:
            label = t(f"section_{dom}")
            s = all_stats[dom]
            st.caption(
                f"**{label}** — {s['documents']} docs · {s['chunks']} chunks"
            )

        with st.expander(t("db_indexed_docs")):
            for dom in DOMAINS:
                label = t(f"section_{dom}")
                st.caption(f"**{label}**")
                if all_stats[dom]["sources"]:
                    for src in all_stats[dom]["sources"]:
                        st.caption(f"- {src}")

        st.markdown("---")

        # Annexes (pages secondaires)
        with st.expander(t("annexes_title")):
            if st.button(
                t("page_upload"), key="btn_upload", use_container_width=True
            ):
                st.session_state.current_page = "upload"
                st.rerun()
            if st.button(
                t("page_matrix"), key="btn_matrix", use_container_width=True
            ):
                st.session_state.current_page = "matrix"
                st.rerun()

        st.markdown("---")

        # Version
        st.markdown(t("version_info"))
        st.markdown("")
        st.markdown(
            "© 2025 Eric QUEAU — "
            "[MIT License](https://opensource.org/licenses/MIT)"
        )
