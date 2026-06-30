from .modelos import Conta, TipoConta

contas = [
    Conta(
        id=1,
        titular="João",
        tipo=TipoConta.CORRENTE,
        saldo=1000.0
    ),
    Conta(
        id=2,
        titular="Maria",
        tipo=TipoConta.CORRENTE,
        saldo=50.0
    ),
    Conta(
        id=3,
        titular="José",
        tipo=TipoConta.POUPANCA,
        saldo=800.0
    ),
    Conta(
        id=4,
        titular="Ana",
        tipo=TipoConta.POUPANCA,
        saldo=100.0
    ),
]