from rich import inspect
class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome:str = nome
        self.idade:int = idade
    def fazer_aniversario(self):
        self.idade += 1

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    def fazer_matricula(self):
        print(f'{self.nome} acabou de fazer matrícula.')
    

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    def dar_aula(self):
        print(f'Prof.{self.nome} começou a dar aula.')

class Funcionario(Pessoa):
    def __init__(self, nome:str, idade:int, cargo:str, setor:str):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    def bater_ponto(self):
        print(f'{self.nome} acabou de bater o ponto.')


a1 = Aluno('Gabriel', 12, 'Programação', 'A')
a1.fazer_aniversario()
p1 = Professor('Samuel', 29, 'Biologia', 'Mestrado')
p1.fazer_aniversario()
f1 = Funcionario('Cláudia', 30, 'Secretária', 'Secretaria')
a1.fazer_matricula()
p1.dar_aula()
f1.bater_ponto()
