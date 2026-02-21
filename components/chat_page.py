"""Page principale : chat RAG avec les documents."""
import streamlit as st

from config import DOMAINS
from core.generation import stream_rag_response
from core.ingestion import get_db_stats
from utils.translations import t


def render_chat_page():
    """Affiche l'interface de chat RAG."""
    domain = st.session_state.get("domain", "medical")
    collection_name = DOMAINS[domain]["collection"]
    msg_key = f"chat_messages_{domain}"
    src_key = f"chat_sources_{domain}"

    stats = get_db_stats(collection_name=collection_name)
    if stats["chunks"] == 0:
        st.warning(t("no_documents"))
        return

    # Bouton clear (petit, en haut)
    if st.button(t("chat_clear"), type="secondary"):
        st.session_state[msg_key] = []
        st.session_state[src_key] = []
        st.rerun()

    # Message d'accueil avec exemples
    if not st.session_state[msg_key]:
        st.info(t(f"chat_welcome_{domain}"))

    # Historique des messages
    for i, msg in enumerate(st.session_state[msg_key]):
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg["role"] == "assistant" and i < len(st.session_state[src_key]):
                sources = st.session_state[src_key][i]
                if sources:
                    _render_sources(sources)

    # Input chat
    if prompt := st.chat_input(t("chat_placeholder")):
        st.session_state[msg_key].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Placeholder sources pour le message user
        st.session_state[src_key].append(None)

        with st.chat_message("assistant"):
            response_chunks = []
            source_chunks = []

            def response_generator():
                for text_chunk, sources in stream_rag_response(
                    prompt,
                    st.session_state[msg_key],
                    domain=domain,
                    collection_name=collection_name,
                ):
                    response_chunks.append(text_chunk)
                    if sources:
                        source_chunks.clear()
                        source_chunks.extend(sources)
                    yield text_chunk

            st.write_stream(response_generator())

            if source_chunks:
                _render_sources(source_chunks)

        full_response = "".join(response_chunks)
        st.session_state[msg_key].append(
            {"role": "assistant", "content": full_response}
        )
        st.session_state[src_key].append(source_chunks)


def _render_sources(chunks: list[dict]):
    """Affiche les sources utilisées pour une réponse."""
    with st.expander(f"{t('sources_title')} ({len(chunks)})"):
        for i, chunk in enumerate(chunks, 1):
            similarity = max(0, 1 - chunk.get("distance", 1))
            st.markdown(
                f'<div class="source-card">'
                f"<strong>[{i}] {chunk['source']}</strong> — "
                f"{t('sources_page')} {chunk['page'] + 1} "
                f"({t('sources_relevance')} : {similarity:.0%})<br>"
                f"<em>{chunk['text'][:200]}...</em>"
                f"</div>",
                unsafe_allow_html=True,
            )
