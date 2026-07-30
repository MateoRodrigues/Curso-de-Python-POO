import time

from rich.panel import Panel
from rich.progress import BarColumn, Progress
from rich.table import Table
from rich.text import Text
from rich.traceback import install

from rich import print

install()

class ControleRemoto:
    # Atributo de classe
    canais: str = '1 2 3 4 5'
    volume: str =  '1,2,3,4,5'
    TV = False
    # Construtor
    def __init__(self) -> None:

        # Atributo de instância
        self.tabela:Table = Table(box=None)
        self.barra_progresso = Progress(BarColumn())
        self.canais = ControleRemoto.canais
        self.barra_progresso_volume = self.barra_progresso.add_task(" ",total=1000)
        self.tabela.add_row('Canal', '=', self.canais)
        self.tabela.add_row('Volume', '=',self.barra_progresso)
        self.canal:int = 0 
        self.canal_volume = Text(f' < CH{str(ControleRemoto.volume[0])} >  - VOL{str(ControleRemoto.canais[0])} + ')
        self.comando:str = ''
   
        while not self.comando == '0':
                time.sleep(0.4)
                self.build_panel()
                print(self.canal_volume, end=' ')
                self.comando = input()
                self.state()
    def state(self) -> None:
        if ControleRemoto.TV:
            if self.comando == '+':
                self.aumentar_volume()
            elif self.comando == '-':
                self.diminuir_volume()
            elif self.comando == '>':
                self.aumentar_canal()
            elif self.comando == '<':
                self.diminuir_canal()
        if self.comando == '@':
            ControleRemoto.TV: bool = not ControleRemoto.TV

    def build_panel(self) -> Panel:
        self.panel = Panel(renderable=self.build_conteudo_panel(),title='[TV]', title_align='center', width=40)
        print(self.panel)

    def build_conteudo_panel(self) -> Table | str:
        if not ControleRemoto.TV:
            return ':no_entry_sign:[red] A TV está desligada!'
        else:
            self.build_tabela()
            return self.tabela
    def build_tabela(self) -> None:
        pass
    def aumentar_volume(self) -> None:
        self.barra_progresso.update(self.barra_progresso_volume,advance=250)
    def diminuir_volume(self) -> None:
        self.barra_progresso.update(self.barra_progresso_volume,advance=-250)
    def aumentar_canal(self):
        # soma canal + 1 se for menor que o tamanho da string porque o último índice é len - 1
        self.canal = self.canal + 1 if self.canal  < len(self.canais)-1 else len(ControleRemoto.canais)-1
        for canal in ControleRemoto.canais.split():
            c = int(canal)
            if c == self.canal+1:
                print(type(canal))
                self.canais += '[white]'
                self.canais +=  str(canal)
                self.canais += '[/]'
            else:
                self.canais += canal

        
    def diminuir_canal(self):
        self.canal = self.canal - 1 if self.canal > 0 else 0
        print(ControleRemoto.canais[self.canal])



# Boa prática de programação mas não é regra de sintaxe
def main():
    # Instanciação
    controle_remoto = ControleRemoto()



# Condição para saber se o arquivo está sendo executado diretamente  OBS: só executa diretamente com este comando 
# Para executá-lo indiretamente apague o if e execute a função main 
if __name__ == '__main__':
    main()


