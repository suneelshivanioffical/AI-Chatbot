import streamlit as st
from chatbot_gemini import get_gemini_response

st.set_page_config(page_title="Gemini Chatbot")

st.title("🤖 Gemini AI Chatbot")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("⚙️ Settings")

    # ---- MODEL SELECTION (ABOVE API KEY) ----
    model_name = st.selectbox(
        "Select Model",
        [
            "gemini-2.5-flash",
        ]
    )

    # ---- API KEY INPUT ----
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""

    api_key_input = st.text_input(
        "Enter your Gemini API Key:",
        type="password"
    )

    if api_key_input:
        st.session_state.api_key = api_key_input

    if not st.session_state.api_key:
        st.warning("Please enter your API key.")
        st.stop()

api_key = st.session_state.api_key

# ------------- CHAT MEMORY --------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# ------------- CHAT INPUT ---------------
if prompt := st.chat_input("Ask something..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        reply = get_gemini_response(api_key, prompt, model_name)

        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write(reply)

    except Exception as e:
        st.error("API Error. Check your key or model.")
        st.exception(e)