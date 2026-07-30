from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.console import Group
from rich import inspect
class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco
        #self.texto = Text(f'{self.nome}', justify='center')
        self.tamanho_texto = len(self.nome)
    def etiqueta(self):
        self.nome_apresentar = Align.center(f'{self.nome}'.center(self.tamanho_texto))
        self.num_separador = 40
        self.separador = f'{'-'* self.num_separador}'
        self.preco_apresentar = Align.center(f'{self.preco:,.2f}'.center(self.num_separador,'.'))
        conteudo = Group(self.nome_apresentar, self.separador,self.preco_apresentar)
        self.panel = (Panel(renderable=conteudo,
                            title=f'{self.__class__.__name__}',
                            title_align='center',
                            padding=(0,0),
                            expand=False,
                            ))
        print(self.panel)



p1 = Produto('Computador', 2000.00)
p1.etiqueta()
p2 = Produto('Mouse', 30)
p2.etiqueta()
p3 = Produto('Máquina de lavar-roupa', 3000.00)
p3.etiqueta()

