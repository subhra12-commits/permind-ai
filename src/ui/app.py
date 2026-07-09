import time
import requests
import streamlit as st

from config import API_URL, APP_NAME
from styles import load_css
from components import (
    render_header,
    render_sidebar,
    render_user_message,
    render_ai_message,
    render_sources
)

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🤖",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

sidebar_state = render_sidebar()

if sidebar_state["new_chat"]:
    st.session_state.messages = []
    st.rerun()

render_header()

for message in st.session_state.messages:
    if message["role"] == "user":
        render_user_message(message["content"])
    else:
        render_ai_message(message["content"])

        if sidebar_state["show_sources"] and message.get("sources"):
            render_sources(message["sources"])

question = st.chat_input("Ask an interview question...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    render_user_message(question)

    with st.spinner("PrepMind AI is thinking..."):
        start_time = time.time()

        try:
            response = requests.post(
                API_URL,
                json={"question": question},
                timeout=120
            )

            response_time = round(time.time() - start_time, 2)

            if response.status_code == 200:
                data = response.json()

                answer = data["answer"]
                sources = data["retrieved_sources"]

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": sources,
                    "response_time": response_time
                })

                render_ai_message(answer)

                st.caption(f"Response time: {response_time} seconds")

                if sidebar_state["show_sources"]:
                    render_sources(sources)

            else:
                st.error(f"API Error: {response.status_code}")
                st.code(response.text)

        except requests.exceptions.ConnectionError:
            st.error(
                "FastAPI backend is not running. Start it first using: "
                "uvicorn src.api.main:app --reload"
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")