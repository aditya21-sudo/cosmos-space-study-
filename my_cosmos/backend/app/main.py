"""My COSMOS API. Run from my_cosmos/backend:  uvicorn app.main:app --reload --port 8020"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import assistant, graph, opportunities, papers_api, recommend, search, trends

app = FastAPI(title="My COSMOS API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(papers_api.router)
app.include_router(search.router)
app.include_router(recommend.router)
app.include_router(graph.router)
app.include_router(trends.router)
app.include_router(opportunities.router)
app.include_router(assistant.router)


@app.get("/health")
def health():
    return {"status": "ok", "answer_provider": assistant.PROVIDER.name}
