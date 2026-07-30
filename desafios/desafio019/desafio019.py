from rich import print
from rich.emoji import EMOJI
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        self.mensagem_inicial = f':open_book: [blue]Você acabou de abrir o livro [red]{self.titulo}[/] que tem [green]{self.paginas} páginas[/] no total. você está na [yellow]página {self.pagina_atual}'
        self.mensagem_final = f':police_car_light: [red]Você chegou ao final do livro {self.titulo}[/]'
        print(self.mensagem_inicial)
        self.pagina_avancadas_max = 0
 

    def __str__(self):
        return f'O titulo do livro é [blue] {self.titulo} [/], tem {self.paginas} paginas'
    
    def avancar_paginas(self, quant_paginas: int = 1):
        self.pagina_passada = self.pagina_atual
        self.pagina_atual += quant_paginas
        cont = 0
        if self.pagina_avancadas_max < self.paginas:
            for p in range(self.pagina_passada+1,self.pagina_atual+1, 1):
                print(f'Pág{p} :arrow_forward:',end=' ')
                cont += 1
                sleep(0.5)
                if p == self.paginas:
                    self.pagina_avancadas_max = p
                    break
            print(f'[blue]Você avançou {cont} páginas e agora está na[/] [yellow]página {self.pagina_atual if self.pagina_atual <=self.paginas else self.paginas}[/]')
            if p == self.paginas:
                print(self.mensagem_final)

    
l1 = Livro('Pequeno Princípe', 60)
l1.avancar_paginas(10)
l1.avancar_paginas(12)
l1.avancar_paginas(10)
l1.avancar_paginas(10)
l1.avancar_paginas(123)
