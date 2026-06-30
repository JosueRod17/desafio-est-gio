from .dados import contas
from .modelos import TipoConta


def procurar_conta(id_conta: int):
    for conta in contas:
        if conta.id == id_conta:
            return conta
    return None


def listar_contas():
    return contas


def sacar(id_conta: int, valor: float):
    conta = procurar_conta(id_conta)

    if conta is None:
        raise ValueError("Conta não encontrada.")

    tarifa = 0

    if conta.tipo == TipoConta.CORRENTE:
        tarifa = 1

        if conta.saldo - (valor + tarifa) < -500:
            raise ValueError("Limite do cheque especial excedido.")

        conta.saldo -= (valor + tarifa)

    else:

        if conta.saldo < valor:
            raise ValueError("Saldo insuficiente.")

        conta.saldo -= valor

    return conta


def transferir(id_origem: int, id_destino: int, valor: float):

    origem = procurar_conta(id_origem)
    destino = procurar_conta(id_destino)

    if origem is None:
        raise ValueError("Conta de origem não encontrada.")

    if destino is None:
        raise ValueError("Conta de destino não encontrada.")

    tarifa = 0

    if origem.tipo == TipoConta.CORRENTE:
        tarifa = 1

        if origem.saldo - (valor + tarifa) < -500:
            raise ValueError("Limite do cheque especial excedido.")

        origem.saldo -= (valor + tarifa)

    else:

        if origem.saldo < valor:
            raise ValueError("Saldo insuficiente.")

        origem.saldo -= valor

    destino.saldo += valor

    return {
        "mensagem": "Transferência realizada com sucesso."
    }