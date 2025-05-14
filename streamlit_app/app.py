import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import requests
from agents.voice_agent import text_to_speech  # now works on Streamlit Cloud

st.set_page_config(page_title="🎙️ Market Assistant", layout="centered")
st.title("🤖 Morning Market Brief Assistant")

query = st.text_input("💬 Ask a market question", placeholder="e.g., What's our Asia tech risk exposure today?")

if st.button("🔍 Get Market Brief"):
    if query:
        with st.spinner("Querying market agents..."):
            try:
                response = requests.post(
                    "http://localhost:8000/query",  # NOTE: only works locally
                    json={"query": query}
                )

                st.code(response.text, language='json')

                result = response.json()["response"]
                st.success(result)

                st.audio(text_to_speech(result), format="audio/mp3")

            except Exception as e:
                st.error(f"Error: {e}")

# Simulate real output
result = """
📊 Stock Movements:
- TSMC: +3.2%
- Samsung: -1.1%

💡 Earnings:
- TSM beat estimates by 4.3%
- Samsung missed by 2.0%
"""
st.success(result)
st.audio(text_to_speech(result), format="audio/mp3")