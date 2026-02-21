"""Système de traduction bilingue FR/EN."""
import streamlit as st

TRANSLATIONS: dict[str, dict[str, str]] = {
    # --- App ---
    "app_title": {
        "fr": "Normes médicales et statistiques",
        "en": "Medical & Statistical Standards",
    },
    "app_subtitle": {
        "fr": "Assistant intelligent pour l'analyse de documents réglementaires",
        "en": "Intelligent assistant for regulatory document analysis",
    },
    # --- Domain selector ---
    "domain_label": {
        "fr": "Domaine",
        "en": "Domain",
    },
    "domain_medical": {
        "fr": "Normes médicales",
        "en": "Medical standards",
    },
    "domain_statistique": {
        "fr": "Normes statistiques",
        "en": "Statistical standards",
    },
    # --- Sidebar ---
    "sidebar_title": {
        "fr": "Navigation",
        "en": "Navigation",
    },
    "page_chat": {
        "fr": "Chat documents",
        "en": "Document chat",
    },
    "page_upload": {
        "fr": "Gestion des documents",
        "en": "Document management",
    },
    "page_matrix": {
        "fr": "Matrice de compliance",
        "en": "Compliance matrix",
    },
    "page_about": {
        "fr": "À propos",
        "en": "About",
    },
    "page_normes_medical": {
        "fr": "Normes médicales",
        "en": "Medical standards",
    },
    "page_normes_statistique": {
        "fr": "Normes statistiques",
        "en": "Statistical standards",
    },
    "page_chat_medical": {
        "fr": "Chat médical",
        "en": "Medical chat",
    },
    "page_chat_statistique": {
        "fr": "Chat statistique",
        "en": "Statistical chat",
    },
    "section_medical": {
        "fr": "Médical",
        "en": "Medical",
    },
    "section_statistique": {
        "fr": "Statistique",
        "en": "Statistical",
    },
    "annexes_title": {
        "fr": "Annexes",
        "en": "Annexes",
    },
    "db_stats_title": {
        "fr": "Base de connaissances",
        "en": "Knowledge base",
    },
    "db_docs": {
        "fr": "Documents",
        "en": "Documents",
    },
    "db_chunks": {
        "fr": "Chunks",
        "en": "Chunks",
    },
    "db_indexed_docs": {
        "fr": "Documents indexés",
        "en": "Indexed documents",
    },
    "lang_label": {
        "fr": "Langue / Language",
        "en": "Language / Langue",
    },
    "version_info": {
        "fr": (
            "**Version 0.3.0** — Fév 2026\n\n"
            "**Nouveautés :**\n"
            "- Double domaine (médical + statistique)\n"
            "- Sélecteur de domaine\n"
            "- Base vectorielle pré-indexée\n"
            "- Synchronisation depuis dossier"
        ),
        "en": (
            "**Version 0.3.0** — Feb 2026\n\n"
            "**New features:**\n"
            "- Dual domain (medical + statistical)\n"
            "- Domain selector\n"
            "- Pre-indexed vector store\n"
            "- Directory sync"
        ),
    },
    # --- Upload page ---
    "upload_title": {
        "fr": "Charger des documents PDF",
        "en": "Upload PDF documents",
    },
    "upload_help": {
        "fr": "Glissez vos fichiers PDF ici (FDA, ISO, IEC...)",
        "en": "Drop your PDF files here (FDA, ISO, IEC...)",
    },
    "upload_domain_hint_medical": {
        "fr": "Les documents seront indexés dans le domaine **normes médicales**.",
        "en": "Documents will be indexed in the **medical standards** domain.",
    },
    "upload_domain_hint_statistique": {
        "fr": "Les documents seront indexés dans le domaine **normes statistiques**.",
        "en": "Documents will be indexed in the **statistical standards** domain.",
    },
    "upload_sync_button": {
        "fr": "Synchroniser depuis le dossier",
        "en": "Sync from directory",
    },
    "upload_sync_processing": {
        "fr": "Synchronisation en cours...",
        "en": "Syncing...",
    },
    "upload_sync_done": {
        "fr": "fichier(s) indexé(s) depuis le dossier",
        "en": "file(s) indexed from directory",
    },
    "upload_sync_uptodate": {
        "fr": "Tous les documents du dossier sont déjà indexés.",
        "en": "All documents from the directory are already indexed.",
    },
    "upload_sync_no_dir": {
        "fr": "Dossier source introuvable.",
        "en": "Source directory not found.",
    },
    "upload_button": {
        "fr": "Indexer les documents",
        "en": "Index documents",
    },
    "upload_success": {
        "fr": "documents indexés avec succès",
        "en": "documents indexed successfully",
    },
    "upload_processing": {
        "fr": "Indexation en cours...",
        "en": "Indexing in progress...",
    },
    "upload_done": {
        "fr": "Terminé !",
        "en": "Done!",
    },
    "upload_delete": {
        "fr": "Supprimer",
        "en": "Delete",
    },
    "upload_deleted": {
        "fr": "supprimé",
        "en": "deleted",
    },
    # --- Chat page ---
    "chat_placeholder": {
        "fr": "Posez une question sur les documents chargés...",
        "en": "Ask a question about uploaded documents...",
    },
    "chat_welcome_medical": {
        "fr": (
            "Posez une question sur les documents médicaux chargés. Exemples :\n"
            "- Quelles sont les exigences de design controls selon la FDA ?\n"
            "- Que dit la FDA sur la validation des procédés ?\n"
            "- Quelles sont les exigences de cybersécurité pour les dispositifs médicaux ?"
        ),
        "en": (
            "Ask a question about the uploaded medical documents. Examples:\n"
            "- What are the FDA design control requirements?\n"
            "- What does the FDA say about process validation?\n"
            "- What are the cybersecurity requirements for medical devices?"
        ),
    },
    "chat_welcome_statistique": {
        "fr": (
            "Posez une question sur les documents statistiques chargés. Exemples :\n"
            "- Quel est le plan d'échantillonnage pour un NQA de 1.0 selon l'ISO 2859-1 ?\n"
            "- Comment calculer les limites de contrôle d'une carte X-barre ?\n"
            "- Quels sont les indices de capabilité Cp et Cpk selon l'ISO 22514 ?"
        ),
        "en": (
            "Ask a question about the uploaded statistical documents. Examples:\n"
            "- What is the sampling plan for an AQL of 1.0 per ISO 2859-1?\n"
            "- How to compute control limits for an X-bar chart?\n"
            "- What are the Cp and Cpk capability indices per ISO 22514?"
        ),
    },
    "chat_clear": {
        "fr": "Effacer la conversation",
        "en": "Clear conversation",
    },
    "chat_error": {
        "fr": "Erreur lors de la génération",
        "en": "Error during generation",
    },
    "chat_api_missing": {
        "fr": "Clé API Groq non configurée. Ajoutez GROQ_API_KEY dans les secrets.",
        "en": "Groq API key not configured. Add GROQ_API_KEY in secrets.",
    },
    "sources_title": {
        "fr": "Sources",
        "en": "Sources",
    },
    "sources_relevance": {
        "fr": "pertinence",
        "en": "relevance",
    },
    "sources_page": {
        "fr": "page",
        "en": "page",
    },
    "no_documents": {
        "fr": "Aucun document indexé. Chargez des PDFs via Annexes > Gestion des documents.",
        "en": "No documents indexed. Upload PDFs via Annexes > Document management.",
    },
    # --- Matrix page ---
    "matrix_title": {
        "fr": "Matrice de compliance",
        "en": "Compliance matrix",
    },
    "matrix_help": {
        "fr": "Croisez les exigences d'un référentiel avec vos procédures internes.",
        "en": "Cross-reference standard requirements with your internal procedures.",
    },
    "matrix_standard": {
        "fr": "Référentiel",
        "en": "Standard",
    },
    "matrix_requirements_for": {
        "fr": "Exigences",
        "en": "Requirements",
    },
    "matrix_requirement": {
        "fr": "Exigence",
        "en": "Requirement",
    },
    "matrix_status": {
        "fr": "Statut",
        "en": "Status",
    },
    "matrix_gap": {
        "fr": "Écart identifié",
        "en": "Gap identified",
    },
    "matrix_corrective_action": {
        "fr": "Action corrective",
        "en": "Corrective action",
    },
    "matrix_add_rows_hint": {
        "fr": "Ajoutez des lignes avec le bouton '+' en bas du tableau.",
        "en": "Add rows with the '+' button at the bottom of the table.",
    },
    "matrix_summary": {
        "fr": "Synthèse",
        "en": "Summary",
    },
    "matrix_compliant": {
        "fr": "Conforme",
        "en": "Compliant",
    },
    "matrix_partial": {
        "fr": "Partiel",
        "en": "Partial",
    },
    "matrix_non_compliant": {
        "fr": "Non conforme",
        "en": "Non-compliant",
    },
    "matrix_to_evaluate": {
        "fr": "À évaluer",
        "en": "To evaluate",
    },
    "matrix_search_title": {
        "fr": "Recherche dans les documents indexés",
        "en": "Search in indexed documents",
    },
    "matrix_search_placeholder_medical": {
        "fr": "ex: design controls, process validation, CAPA...",
        "en": "e.g.: design controls, process validation, CAPA...",
    },
    "matrix_search_placeholder_statistique": {
        "fr": "ex: plan d'échantillonnage, NQA, carte de contrôle, capabilité...",
        "en": "e.g.: sampling plan, AQL, control chart, capability...",
    },
    "matrix_search_label": {
        "fr": "Rechercher dans les documents chargés",
        "en": "Search in uploaded documents",
    },
    "matrix_searching": {
        "fr": "Recherche en cours...",
        "en": "Searching...",
    },
    "matrix_no_results": {
        "fr": "Aucun résultat. Vérifiez que des documents sont indexés.",
        "en": "No results. Check that documents are indexed.",
    },
    "matrix_custom_empty": {
        "fr": "Personnalisé (vide)",
        "en": "Custom (empty)",
    },
    # --- About page : domains ---
    "about_domains_title": {
        "fr": "Domaines étudiés",
        "en": "Domains covered",
    },
    "about_domain_medical_desc": {
        "fr": (
            "Normes et réglementations pour les dispositifs médicaux : "
            "FDA 21 CFR 820, ISO 13485, IEC 62304, EU MDR, cybersécurité..."
        ),
        "en": (
            "Standards and regulations for medical devices: "
            "FDA 21 CFR 820, ISO 13485, IEC 62304, EU MDR, cybersecurity..."
        ),
    },
    "about_domain_statistique_desc": {
        "fr": (
            "Normes statistiques industrielles : échantillonnage (ISO 2859, ISO 3951), "
            "cartes de contrôle SPC (ISO 7870), capabilité des procédés (ISO 22514), "
            "interprétation statistique des données (ISO 16269)."
        ),
        "en": (
            "Industrial statistical standards: sampling (ISO 2859, ISO 3951), "
            "SPC control charts (ISO 7870), process capability (ISO 22514), "
            "statistical interpretation of data (ISO 16269)."
        ),
    },
}


def t(key: str) -> str:
    """Retourne la traduction pour la langue courante."""
    lang = st.session_state.get("lang", "fr")
    entry = TRANSLATIONS.get(key, {})
    return entry.get(lang, entry.get("fr", key))
