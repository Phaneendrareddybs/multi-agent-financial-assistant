import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import requests

# from agents.voice_agent import text_to_speech  # ❌ Whisper not supported in Streamlit Cloud

st.set_page_config(page_title="🎙️ Market Assistant", layout="centered")
st.title("🤖 Morning Market Brief Assistant")

query = st.text_input("💬 Ask a market question", placeholder="e.g., What's our Asia tech risk exposure today?")

if st.button("🔍 Get Market Brief"):
    if query:
        with st.spinner("Querying market agents..."):
            try:
                # Simulated output
                result = """
📊 Stock Movements:
- TSMC: +3.2%
- Samsung: -1.1%

💡 Earnings:
- TSM beat estimates by 4.3%
- Samsung missed by 2.0%
"""
                st.success(result)
                st.write("🗣️ Voice synthesis disabled for this live demo.")

            except Exception as e:
                st.error(f"Error: {e}")
