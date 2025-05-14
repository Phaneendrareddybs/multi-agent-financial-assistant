
# 🧠 Multi-Agent Financial Assistant

A real-time, modular voice-enabled financial assistant that provides spoken or text-based market summaries. Built using FastAPI, LangChain, OpenAI, FAISS, and deployed using Streamlit Cloud and Render.

---

## 🔗 Live Demos

- 🌐 **Streamlit Frontend**: [https://your-app.streamlit.app](https://your-app.streamlit.app)
- ⚙️ **FastAPI Backend (Render)**: [https://multi-agent-api.onrender.com/docs](https://multi-agent-api.onrender.com/docs)
- 💻 **GitHub Repo**: [https://github.com/Phaneendrareddybs/multi-agent-financial-assistant](https://github.com/Phaneendrareddybs/multi-agent-financial-assistant)

---

## 📦 Features

- ✅ Real-time stock data via Alpha Vantage
- ✅ Earnings surprise detection (TSMC & Samsung)
- ✅ Retrieval-Augmented Generation using LangChain + FAISS
- ✅ Modular architecture with FastAPI microservices
- ✅ Voice synthesis pipeline using Whisper and gTTS (disabled in cloud)
- ✅ Deployed Streamlit UI for interactive usage

---

## 🧠 Agent Architecture

```
[User Input]
     |
[Streamlit Frontend]
     |
[FastAPI Orchestrator]
 ┌────┬────────┬────────────┐
 │ API Agent  Scraper Agent │
 │ Retriever Agent          │
 └────┴────────┴────────────┘
     |
[LangChain + OpenAI]
     |
[Text Response] -> [TTS (Optional)]
```

---

## 📁 Project Structure

```
multi-agent-financial-assistant/
├── agents/
│   ├── api_agent.py
│   ├── scraping_agent.py
│   ├── retriever_agent.py
│   ├── language_agent.py
│   └── voice_agent.py
├── orchestrator/
│   └── orchestrator.py
├── streamlit_app/
│   └── app.py
├── docs/
│   └── ai_tool_usage.md
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/Phaneendrareddybs/multi-agent-financial-assistant.git
cd multi-agent-financial-assistant

# Install dependencies
pip install -r requirements.txt

# Run FastAPI backend
uvicorn orchestrator.orchestrator:app --reload

# Run frontend
streamlit run streamlit_app/app.py
```

---

## 🔐 Environment Variables

Set the OpenAI key in `.env` or environment settings:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

On Render, this is added in the **Environment tab**.

---

## 📄 AI Tool Usage

See [`docs/ai_tool_usage.md`](docs/ai_tool_usage.md) for full documentation of:

- LLM integration
- RAG configuration
- Prompt structure
- Tool usage steps

---

## 🎤 Voice Synthesis

Voice input and output (Whisper + gTTS) are supported locally.  
Due to limitations, this feature is disabled in the cloud deployment.

---

## 🧪 Tech Stack

- LangChain, OpenAI GPT
- Alpha Vantage & yFinance
- FAISS for vector search
- FastAPI, Streamlit
- Deployed on Render + Streamlit Cloud

---

## 📬 License & Credits

Open-source project developed by [Phaneendra Reddy B S](https://github.com/Phaneendrareddybs).  
Licensed under MIT. Inspired by OpenAI agent architecture.

---
