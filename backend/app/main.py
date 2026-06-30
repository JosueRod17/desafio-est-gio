from typing import List
from fastapi import FastAPI
from .dados import contas
from .modelos import Conta

app = FastAPI(
    title="Banco Agilize API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "API funcionando!"}


@app.get("/contas", response_model=List[Conta])
def listar_contas():
    return contas