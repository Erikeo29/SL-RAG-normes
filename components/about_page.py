"""Page a propos : description du projet et architecture."""
import streamlit as st

from config import DOMAINS
from core.ingestion import get_db_stats
from utils.translations import t


def render_about_page():
    """Affiche la page a propos."""
    lang = st.session_state.get("lang", "fr")

    # Stats par domaine
    stats_by_domain = {}
    for dom, cfg in DOMAINS.items():
        stats_by_domain[dom] = get_db_stats(collection_name=cfg["collection"])

    if lang == "fr":
        _render_fr(stats_by_domain)
    else:
        _render_en(stats_by_domain)


def _render_fr(stats_by_domain: dict[str, dict]):
    st.header("A propos")

    st.subheader("Objectif")
    st.markdown(
        "Cette application est un **assistant intelligent** pour l'analyse de documents "
        "reglementaires. Elle utilise la technologie **RAG** (Retrieval-Augmented Generation) "
        "pour permettre de poser des questions en langage naturel sur les documents charges."
    )

    st.subheader(t("about_domains_title"))
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**{DOMAINS['medical']['icon']} {t('domain_medical')}**")
        st.markdown(t("about_domain_medical_desc"))
        stats = stats_by_domain["medical"]
        st.caption(f"{stats['documents']} documents, {stats['chunks']} chunks")
    with col2:
        st.markdown(f"**{DOMAINS['statistique']['icon']} {t('domain_statistique')}**")
        st.markdown(t("about_domain_statistique_desc"))
        stats = stats_by_domain["statistique"]
        st.caption(f"{stats['documents']} documents, {stats['chunks']} chunks")

    st.subheader("Architecture")
    st.code(
        "PDF Upload -> Decoupage en chunks -> Embeddings -> ChromaDB\n"
        "                                                      |\n"
        "Question -> Embedding -> Recherche semantique -> Chunks pertinents\n"
        "                                                      |\n"
        "               Chunks + Question -> LLM (Llama 3.3) -> Reponse sourcee",
        language=None,
    )

    st.subheader("Composants techniques")
    st.markdown(
        "| Composant | Technologie |\n"
        "|-----------|-------------|\n"
        "| Interface | Streamlit |\n"
        "| Embeddings | ChromaDB ONNX (all-MiniLM-L6-v2) |\n"
        "| Base vectorielle | ChromaDB (persistante, locale) |\n"
        "| LLM | Llama 3.3 70B via Groq API |\n"
        "| PDF parsing | PyPDF |\n"
        "| Chunking | LangChain RecursiveCharacterTextSplitter |"
    )

    st.subheader("Documents actuellement indexes")
    for dom, cfg in DOMAINS.items():
        stats = stats_by_domain[dom]
        label = t(f"domain_{dom}")
        st.markdown(f"**{cfg['icon']} {label}**")
        if stats["sources"]:
            for src in stats["sources"]:
                st.markdown(f"- {src}")
            st.caption(f"{stats['documents']} documents, {stats['chunks']} chunks")
        else:
            st.caption("Aucun document indexe.")

    st.subheader("Fonctionnalites")
    st.markdown(
        "- **Selecteur de domaine** : basculez entre normes medicales et normes statistiques\n"
        "- **Chat RAG** : posez des questions en langage naturel, obtenez des reponses "
        "avec references aux documents sources\n"
        "- **Gestion des documents** : upload, indexation et suppression de PDFs par domaine\n"
        "- **Matrice de compliance** : evaluez la conformite par referentiel "
        "(FDA, ISO statistiques...) avec recherche RAG integree\n"
        "- **Bilingue** : francais et anglais"
    )

    st.subheader("Cas d'usage")
    st.markdown(
        "- Recherche rapide d'exigences dans les documents reglementaires charges\n"
        "- Preparation d'audits : identifier rapidement les clauses pertinentes\n"
        "- Gap analysis : comparer les exigences avec les procedures internes\n"
        "- Formation : comprendre les exigences reglementaires de maniere interactive"
    )

    st.caption(
        "Note : cette application analyse uniquement les documents que vous chargez. "
        "Les normes ISO (13485, 14971, 2859...) sont sous copyright et doivent etre achetees "
        "aupres de l'ISO. Les documents FDA sont gratuits et telechargeables depuis fda.gov."
    )


def _render_en(stats_by_domain: dict[str, dict]):
    st.header("About")

    st.subheader("Purpose")
    st.markdown(
        "This application is an **intelligent assistant** for analyzing regulatory documents. "
        "It uses **RAG** (Retrieval-Augmented Generation) technology to allow natural language "
        "questions on uploaded documents."
    )

    st.subheader(t("about_domains_title"))
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**{DOMAINS['medical']['icon']} {t('domain_medical')}**")
        st.markdown(t("about_domain_medical_desc"))
        stats = stats_by_domain["medical"]
        st.caption(f"{stats['documents']} documents, {stats['chunks']} chunks")
    with col2:
        st.markdown(f"**{DOMAINS['statistique']['icon']} {t('domain_statistique')}**")
        st.markdown(t("about_domain_statistique_desc"))
        stats = stats_by_domain["statistique"]
        st.caption(f"{stats['documents']} documents, {stats['chunks']} chunks")

    st.subheader("Architecture")
    st.code(
        "PDF Upload -> Chunking -> Embeddings -> ChromaDB\n"
        "                                           |\n"
        "Question -> Embedding -> Semantic search -> Relevant chunks\n"
        "                                           |\n"
        "            Chunks + Question -> LLM (Llama 3.3) -> Sourced answer",
        language=None,
    )

    st.subheader("Technical components")
    st.markdown(
        "| Component | Technology |\n"
        "|-----------|------------|\n"
        "| Interface | Streamlit |\n"
        "| Embeddings | ChromaDB ONNX (all-MiniLM-L6-v2) |\n"
        "| Vector store | ChromaDB (persistent, local) |\n"
        "| LLM | Llama 3.3 70B via Groq API |\n"
        "| PDF parsing | PyPDF |\n"
        "| Chunking | LangChain RecursiveCharacterTextSplitter |"
    )

    st.subheader("Currently indexed documents")
    for dom, cfg in DOMAINS.items():
        stats = stats_by_domain[dom]
        label = t(f"domain_{dom}")
        st.markdown(f"**{cfg['icon']} {label}**")
        if stats["sources"]:
            for src in stats["sources"]:
                st.markdown(f"- {src}")
            st.caption(f"{stats['documents']} documents, {stats['chunks']} chunks")
        else:
            st.caption("No documents indexed.")

    st.subheader("Features")
    st.markdown(
        "- **Domain selector**: switch between medical standards and statistical standards\n"
        "- **RAG Chat**: ask natural language questions, get answers with source references\n"
        "- **Document management**: upload, index and delete PDFs per domain\n"
        "- **Compliance matrix**: assess conformity by standard "
        "(FDA, ISO statistical...) with integrated RAG search\n"
        "- **Bilingual**: French and English"
    )

    st.subheader("Use cases")
    st.markdown(
        "- Quick lookup of requirements in uploaded regulatory documents\n"
        "- Audit preparation: rapidly identify relevant clauses\n"
        "- Gap analysis: compare requirements with internal procedures\n"
        "- Training: understand regulatory requirements interactively"
    )

    st.caption(
        "Note: this application only analyzes documents you upload. "
        "ISO standards (13485, 14971, 2859...) are copyrighted and must be purchased from ISO. "
        "FDA documents are free and downloadable from fda.gov."
    )
