import streamlit as st
from config import APP_NAME, APP_TAGLINE, INTERVIEW_MODES, DEFAULT_MODE


def render_header():
    st.markdown(
        f"""
        <div class="app-header">
            <div class="app-title">🤖 {APP_NAME}</div>
            <div class="app-subtitle">{APP_TAGLINE}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_sidebar():
    with st.sidebar:
        st.markdown(f"## 🤖 {APP_NAME}")
        st.caption("Interview preparation workspace")

        new_chat = st.button("➕ New Interview", use_container_width=True)

        st.markdown("---")

        mode = st.radio(
            "🎯 Interview Mode",
            INTERVIEW_MODES,
            index=INTERVIEW_MODES.index(DEFAULT_MODE)
        )

        st.markdown("---")

        st.markdown("### 📊 Session Stats")

        total_questions = len(st.session_state.get("messages", [])) // 2

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">Questions Asked</div>
                <div class="metric-value">{total_questions}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        show_sources = st.toggle("Show retrieved sources", value=True)

        return {
            "new_chat": new_chat,
            "mode": mode,
            "show_sources": show_sources
        }


def render_user_message(message):
    st.markdown(
        f"""
        <div class="user-bubble">
            <b>You</b><br>
            {message}
        </div>
        """,
        unsafe_allow_html=True
    )


def render_ai_message(message):
    st.markdown(
        f"""
        <div class="ai-bubble">
            <b>PrepMind AI</b><br><br>
            {message}
        </div>
        """,
        unsafe_allow_html=True
    )


def render_sources(sources):
    with st.expander("📚 Retrieved Sources"):
        for i, source in enumerate(sources, start=1):
            st.markdown(
                f"""
                <div class="source-card">
                    <b>Source {i}</b>
                    <div class="source-meta">
                        Score: {source["score"]:.4f} |
                        Category: {source["category"]} |
                        Difficulty: {source["difficulty"]}
                    </div>
                    <b>Question:</b> {source["question"]}<br><br>
                    <b>Dataset:</b> {source["dataset_name"]}
                </div>
                """,
                unsafe_allow_html=True
            )