import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import requests

st.set_page_config(page_title="🎙️ Market Assistant", layout="centered")
st.title("🤖 Morning Market Brief Assistant")

query = st.text_input("💬 Ask a market question", placeholder="e.g., What's our Asia tech risk exposure today?")

if st.button("🔍 Get Market Brief"):
    if query:
        with st.spinner("Querying market agents..."):
            try:
                response = requests.post(
                    "https://multi-agent-api.onrender.com/query",
                    json={"query": query}
                )

                st.code(response.text, language="json")

                result = response.json()["response"]
                st.success(result)
                st.write("🗣️ Voice synthesis disabled for this live demo.")

            except Exception as e:
                st.error(f"❌ Error: {e}")
