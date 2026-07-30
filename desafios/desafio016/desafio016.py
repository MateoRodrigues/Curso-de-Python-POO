from rich import print
class Funcionario:
    # Variável de classe
    empresa :str = 'Curso em Vídeo'
    # Para utilizar na classe faça classe.variável
    def __init__(self, nome: str, setor: str, cargo: str):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def apresentar(self):
        print(f':handshake: Olá, sou [blue]{self.nome}[/] e sou [blue]{self.cargo}[/] do setor de [blue]{self.setor}[/] da empresa [blue]{Funcionario.empresa}[/]')


f1 = Funcionario('Maria','Administração', 'Diretora')
f1.apresentar()