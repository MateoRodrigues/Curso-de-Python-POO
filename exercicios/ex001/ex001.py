# Declaração de classe
class Gafanhoto:
    def __init__(self): #Método contrutor
        # Atributos de instância
        self.nome = ''
        self.idade = 0
    # Métodos de instância
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade "

# Declaração de objetos
g1 = Gafanhoto()
g1.nome = 'Maria'
g1.idade = 10


g2 = Gafanhoto()
g2.nome = 'Carlos'
g2.idade = 30
print(g2.mensagem())
print(g1.mensagem())
g3 = Gafanhoto()
g3.nome = 'Caio'
g3.idade = 13
print(g3.mensagem())
g4 = Gafanhoto()
print(g4.mensagem())