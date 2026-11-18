class ContaBancaria:
    """Cria uma conta bancária que permite fazer saques e depósitos."""
    def __init__(self, id, titular, saldo=0):
        self.id = id
        self.titular = titular
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}')
    def __str__(self):
        return f'A Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo}'
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito  de R${valor:,.2f} autorizado na conta {self.id}')
    def sacar(self, valor:int|float) -> None:
        if valor > self.saldo:
            print(f'Saque NEGADO  de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE')
        else:
            self.saldo -= valor
            print(f'Saque  de R${valor:,.2f} autorizado na conta {self.id}')




c1 = ContaBancaria(112,'Gustavo', 3000)
c1.depositar(500)
c1.sacar(2_000_000)
print(c1)