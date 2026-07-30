from rich import print
from rich.panel import Panel

class ControleRemoto:
    # Atributos de classe
    canal_min:int = 1
    canal_max:int = 5
    volume_min:int = 1
    volume_max:int = 5
    # Construtor
    def __init__(self, canal = 1, volume = 2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False
    def liga_desliga(self):
        self.ligado = not self.ligado
    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1
    def canal_menos(self):
         if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1
    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1
    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1
    def mostrar_TV(self):
        conteudo = ''
        if not self.ligado:
            conteudo = ':prohibited: A TV está desligada'
        else:
            conteudo = 'CANAL  = '
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max+1):
                if canal == self.canal_atual:
                    conteudo += f'[black on white] {canal} [/]'
                else:
                    conteudo += f' {canal} '
            conteudo += '\nVOLUME = '
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max+1):
                if volume <= self.volume_atual:
                    conteudo += '[black on white]   [/]'
                else:
                    conteudo += '[black on black]   [/]'
        tv:Panel = Panel(conteudo, title='[TV]', title_align='center',width=40)
        print(tv)

c1 = ControleRemoto()
while True:
    c1.mostrar_TV()
    comando = str(input(f' < CH{c1.canal_atual}>  - VOL{c1.volume_atual} +'))
    match comando:
        case '0':
            break
        case '@':
            c1.liga_desliga()
        case '>':
            c1.canal_mais()
        case '<':
            c1.canal_menos()
        case '-':
            c1.volume_menos()
        case '+':
            c1.volume_mais()
    #print('\n' * 10)



