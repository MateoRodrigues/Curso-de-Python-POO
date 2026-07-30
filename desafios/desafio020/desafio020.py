from rich import print
from rich.panel import Panel
# :video_game:
class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.list_favoritos = []
        self.conteudo = ''
        self.conteudo += f'Nome real: {self.nome}\n'
        self.conteudo += 'Jogo favoritos: \n'

    def __str__(self):
        return str(self.__dict__)
    def add_favoritos(self,jogo):
        if jogo:
            self.list_favoritos.append(jogo)
        else:
            print('ERRO: Nome inválido!!![/]')
    def ficha(self):
        for texto in self.list_favoritos:
            self.conteudo += f':video_game: [blue]{texto}[/]\n'
        panel = Panel(self.conteudo,title=f'Jogador <{self.nick}>')
        print(panel)

g1 = Gamer('Maurício', 'detonator324')
g1.add_favoritos('Mario Kart')
g1.add_favoritos('FIFA')
g1.add_favoritos('EFootball')
g1.ficha()
