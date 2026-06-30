from enum import Enum
from pydantic import BaseModel


class TipoConta(str, Enum):
    CORRENTE = "corrente"
    POUPANCA = "poupanca"


class Conta(BaseModel):
    id: int
    titular: str
    tipo: TipoConta
    saldo: float