# orchestrator/orchestrator.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from pydantic import BaseModel
from agents.api_agent import get_market_snapshot
from agents.scraping_agent import get_earnings_surprise
from agents.language_agent import generate_market_brief

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def get_response(request: QueryRequest):
    query = request.query

    try:
        market_data = get_market_snapshot()
        tsm_earnings = get_earnings_surprise("TSM")
        samsung_earnings = get_earnings_surprise("005930.KQ")
        rag_summary = generate_market_brief(query)

        combined_response = (
            f"{rag_summary}\n\n"
            f"📊 Stock Movements:\n"
            f"- TSMC: {market_data['TSMC']['change_pct']}% change\n"
            f"- Samsung: {market_data['Samsung']['change_pct']}% change\n\n"
            f"💡 Earnings:\n"
            f"- {tsm_earnings}\n"
            f"- {samsung_earnings}"
        )

        return {"response": combined_response}

    except Exception as e:
        return {"response": f"⚠️ Internal error: {e}"}
