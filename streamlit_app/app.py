import streamlit as st
import requests
from agents.voice_agent import text_to_speech

st.set_page_config(page_title="🎙️ Market Assistant", layout="centered")
st.title("🤖 Morning Market Brief Assistant")

query = st.text_input("💬 Ask a market question", placeholder="e.g., What's our Asia tech risk exposure today?")

if st.button("🔍 Get Market Brief"):
    if query:
        with st.spinner("Querying market agents..."):
            try:
                response = requests.post(
                    "http://localhost:8000/query",
                    json={"query": query}
                )

                # Debugging response
                st.code(response.text, language='json')  # 👈 shows raw server response

                result = response.json()["response"]
                st.success(result)

                st.audio(text_to_speech(result), format="audio/mp3")

            except Exception as e:
                st.error(f"Error: {e}")
