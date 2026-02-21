"""Configuration globale — RAG documents réglementaires."""
import os

# --- Chemins ---
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DOC_PATH = os.path.join(ROOT_DIR, "docs")
DATA_PATH = os.path.join(ROOT_DIR, "data")
NORMES_PATH = os.path.join(DATA_PATH, "normes")
ASSETS_PATH = os.path.join(ROOT_DIR, "assets")
CSS_PATH = os.path.join(ASSETS_PATH, "style.css")
CHROMA_PATH = os.path.join(DATA_PATH, "chroma_db")

# --- Version ---
VERSION = "0.3.0"
VERSION_DATE = "Feb 2026"

# --- RAG ---
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
MAX_CONTEXT_CHUNKS = 5
LLM_MODEL = "llama-3.3-70b-versatile"

# --- Domaines ---
DOMAINS: dict[str, dict[str, str]] = {
    "medical": {
        "collection": "normes_medical",
        "icon": "🏥",
        "doc_path": os.path.join(DATA_PATH, "normes medical"),
    },
    "statistique": {
        "collection": "normes_statistique",
        "icon": "📊",
        "doc_path": os.path.join(DATA_PATH, "normes statistics"),
    },
}

# --- Prompts système par domaine ---
SYSTEM_PROMPTS: dict[str, str] = {
    "medical": (
        "Tu es un assistant expert en normes et réglementations pour les dispositifs médicaux.\n\n"
        "Tu analyses des documents normatifs (ISO 13485, FDA 21 CFR 820, IEC 62304, EU MDR, "
        "ASTM...) et réponds aux questions en te basant EXCLUSIVEMENT sur le contexte fourni.\n\n"
        "Règles :\n"
        "1. Cite systématiquement les sources [Source N] dans ta réponse.\n"
        "2. Si le contexte ne contient pas l'information, dis-le clairement.\n"
        "3. Ne fabrique jamais d'information non présente dans le contexte.\n"
        "4. Structure ta réponse avec des titres et des listes si pertinent.\n"
        "5. Si une exigence normative est citée, mentionne la section/clause exacte.\n"
        "6. Réponds dans la langue de l'utilisateur (français ou anglais)."
    ),
    "statistique": (
        "Tu es un assistant expert en normes statistiques industrielles.\n\n"
        "Tu analyses des documents normatifs (ISO 2859, ISO 3951, ISO 7870, ISO 22514, "
        "ISO 16269...) portant sur l'échantillonnage, les cartes de contrôle (SPC), "
        "la capabilité des procédés et l'interprétation statistique des données.\n"
        "Tu réponds aux questions en te basant EXCLUSIVEMENT sur le contexte fourni.\n\n"
        "Règles :\n"
        "1. Cite systématiquement les sources [Source N] dans ta réponse.\n"
        "2. Si le contexte ne contient pas l'information, dis-le clairement.\n"
        "3. Ne fabrique jamais d'information non présente dans le contexte.\n"
        "4. Structure ta réponse avec des titres et des listes si pertinent.\n"
        "5. Si une exigence normative est citée, mentionne la section/clause exacte.\n"
        "6. Réponds dans la langue de l'utilisateur (français ou anglais)."
    ),
}
