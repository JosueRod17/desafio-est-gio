from .modelos import Conta, TipoConta

contas = [
    Conta(
        id=1,
        titular="Josué",
        tipo=TipoConta.CORRENTE,
        saldo=1000.0
    ),
    Conta(
        id=2,
        titular="Júlia",
        tipo=TipoConta.CORRENTE,
        saldo=50.0
    ),
    Conta(
        id=3,
        titular="José Inácio",
        tipo=TipoConta.POUPANCA,
        saldo=800.0
    ),
    Conta(
        id=4,
        titular="Ana Clara",
        tipo=TipoConta.POUPANCA,
        saldo=100.0
    ),
]