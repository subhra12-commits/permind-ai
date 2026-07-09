def load_css():
    return """
    <style>
    .stApp {
        background: #0f172a;
        color: #e5e7eb;
    }

    .block-container {
        padding-top: 1.5rem;
        max-width: 1200px;
    }

    .app-header {
        background: linear-gradient(135deg, #1e293b, #111827);
        padding: 1.8rem;
        border-radius: 20px;
        border: 1px solid #334155;
        margin-bottom: 1.5rem;
    }

    .app-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.3rem;
    }

    .app-subtitle {
        font-size: 1rem;
        color: #cbd5e1;
    }

    .chat-card {
        background: #111827;
        border: 1px solid #334155;
        border-radius: 18px;
        padding: 1.3rem;
        margin-bottom: 1rem;
    }

    .user-bubble {
        background: #2563eb;
        color: white;
        padding: 1rem;
        border-radius: 16px 16px 4px 16px;
        margin-bottom: 1rem;
        font-size: 1rem;
        line-height: 1.6;
    }

    .ai-bubble {
        background: #ffffff;
        color: #111827;
        padding: 1.2rem;
        border-radius: 16px 16px 16px 4px;
        margin-bottom: 1rem;
        font-size: 1rem;
        line-height: 1.7;
    }

    .source-card {
        background: #1e293b;
        color: #e5e7eb;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 1rem;
        margin-bottom: 0.8rem;
    }

    .source-meta {
        color: #94a3b8;
        font-size: 0.85rem;
        margin-bottom: 0.5rem;
    }

    .metric-card {
        background: #111827;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 1rem;
        margin-bottom: 0.8rem;
    }

    .metric-label {
        color: #94a3b8;
        font-size: 0.85rem;
    }

    .metric-value {
        color: #ffffff;
        font-size: 1.4rem;
        font-weight: 700;
    }

    textarea {
        border-radius: 14px !important;
    }

    .stButton > button {
        background: #2563eb;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 0.7rem 1rem;
        font-weight: 600;
    }

    .stButton > button:hover {
        background: #1d4ed8;
        color: white;
    }
    </style>
    """