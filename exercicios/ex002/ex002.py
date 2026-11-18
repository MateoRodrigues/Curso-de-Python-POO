# Declaração de classe
class Gafanhoto:
    """Esta classe Gafanhoto representa uma pessoa com nome e idade,
    devem ser instanciada da seguinte forma.
    variável = Gafanhoto(nome, idade)"""
    def __init__(self,nome = " ", idade = 0): #Método contrutor
        # Atributos de instância
        self.nome = nome
        self.idade = idade
    # Métodos de instância
    def aniversario(self):
        self.idade += 1
    def __str__(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade "




# Declaração de objetos
g1 = Gafanhoto("Maria", 10)
print(g1.__dict__)
print(g1.__class__)