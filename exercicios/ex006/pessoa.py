class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome:str = nome
        self.idade:int = idade
    def fazer_aniversario(self):
        self.idade += 1