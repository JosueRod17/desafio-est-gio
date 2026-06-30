from fastapi import FastAPI
from .rotas import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Banco Agilize API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "mensagem": "API Banco Agilize funcionando!"
    }