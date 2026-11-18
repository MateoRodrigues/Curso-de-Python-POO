class ContaBancaria:
    """Cria uma conta bancária que permite fazer saques e depósitos."""
    def __init__(self, id:int, titular:str, saldo:float=0):
        self.id = id # público[public(+)]
        self._titular = titular # protegido[protected(#)]
        self.__saldo = saldo # privado[private(-)]
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}')
    def __str__(self):
        #return f'A Conta {self.id} criada com sucesso. Saldo atual de R${self.__saldo}'
        return f'O estado atual é {self.__dict__}'
    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Depósito  de R${valor:,.2f} autorizado na conta {self.id}')
    def sacar(self, valor:float) -> None:
        valor = abs(valor)
        if valor > self.__saldo:
            print(f'Saque NEGADO  de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE')
        else:
            self.__saldo -= valor
            print(f'Saque  de R${valor:,.2f} autorizado na conta {self.id}')




