from rich import print
from rich import inspect
from typing import Literal

class Caneta:
    opcao_cores = Literal['Azul','Verde','Vermelho']
    cores = {'Azul': '[blue]', 'Vermelho': '[red]', 'Verde' : '[green]'}


    def __init__(self, cor : opcao_cores):
        self.cor : Caneta.opcao_cores = cor
        self.tampada : bool = True
        self.texto : str = ''
    def destampar(self):
        self.tampada = False
    def tampar(self):
        self.tampada = True
    def escrever(self, texto : str):
        if not self.tampada:
            self.texto = f'{Caneta.cores[self.cor]} {texto} [/]'
            print(self.texto, end=' ')
    def quebra_linha(self, num_linhas: int) -> None:
        for n_linhas in range(0,num_linhas):
            print()

c1 = Caneta('Verde')
c1.destampar()
c1.escrever('Olá mundo ')
c1.quebra_linha(1)
c1.escrever('Como vc está?')

c2 = Caneta('Vermelho')
c2.destampar()
c2.escrever('Cheguei!!!')




