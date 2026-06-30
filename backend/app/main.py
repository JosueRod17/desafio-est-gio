from fastapi import FastAPI
from .rotas import router

app = FastAPI(
    title="Banco Agilize API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "mensagem": "API Banco Agilize funcionando!"
    }