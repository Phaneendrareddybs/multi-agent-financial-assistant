# agents/language_agent.py

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from agents.retriever_agent import build_vector_index

def generate_market_brief(query):
    retriever = build_vector_index().as_retriever()
    llm = OpenAI(temperature=0)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )

    result = qa_chain.run(query)
    return result

import os
os.environ["OPENAI_API_KEY"] = "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"
