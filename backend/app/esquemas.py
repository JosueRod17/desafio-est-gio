from pydantic import BaseModel, Field


class RequisicaoSaque(BaseModel):
    id_conta: int
    valor: float = Field(gt=0)


class RequisicaoTransferencia(BaseModel):
    id_conta_origem: int
    id_conta_destino: int
    valor: float = Field(gt=0)