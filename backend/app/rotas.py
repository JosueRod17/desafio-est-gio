from fastapi import APIRouter, HTTPException

from .servicos import listar_contas, sacar, transferir
from .esquemas import RequisicaoSaque, RequisicaoTransferencia

router = APIRouter()


@router.get("/contas")
def listar():
    return listar_contas()


@router.post("/saque")
def realizar_saque(requisicao: RequisicaoSaque):
    try:
        return sacar(requisicao.id_conta, requisicao.valor)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))


@router.post("/transferencia")
def realizar_transferencia(requisicao: RequisicaoTransferencia):
    try:
        return transferir(
            requisicao.id_conta_origem,
            requisicao.id_conta_destino,
            requisicao.valor
        )
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))