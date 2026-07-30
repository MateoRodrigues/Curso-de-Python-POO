from rich import print
from rich.panel import Panel
from rich.console import Group


class Churrasco:
    # Variáveis de Classe
    carne_p_pessoa = 400
    preco_carne = 82.40

    def __init__(self, titulo : str, quant: int):
        # Variáveis de instância
        self.titulo = titulo
        self.quant = quant
        self.carne_churrasco = Churrasco.carne_p_pessoa * self.quant
        self.preco_churrasco = Churrasco.preco_carne * self.quant
        self.pessoa_pagar = self.preco_churrasco / self.quant

    def analizar(self):
        self.frase_1 = f' Analizando [green]{self.titulo}[/] com [blue] {self.quant} convidados [/]'
        self.frase_2 = f' Cada participante comerá {Churrasco.carne_p_pessoa/1000} kg e cada kg custa R${Churrasco.preco_carne:.2f}'
        self.frase_3 = f' Recomendo [blue]comprar {self.carne_churrasco/1000:.3f} kg[/] de carne'
        self.frase_4 = f' O custo total será de [green]R${self.preco_churrasco:.2f}[/]'
        self.frase_5 = f' Cada pessoa pagará [yellow]R${self.pessoa_pagar:.2f}[/] para participar.'
        self.conteudo = Group(self.frase_1, self.frase_2, self.frase_3, self.frase_4, self.frase_5)
        self.panel = Panel(renderable=self.conteudo, title=self.titulo, title_align='center', expand=False)
        print(self.panel)





c1 = Churrasco('Churras dos amigos', 10)
c1.analizar()
