from abc import ABC, abstractmethod
from math import pi




class Poligono(ABC):
    def __init__(self, qtd_lados:int):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self,lado:int):
        super().__init__(4) 
        self.lado = lado
    def perimetro(self):
        return self.lado * 4
    def area(self):
        return self.lado ** 2
class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio
    def perimetro(self):
        return 2 * pi * self.raio
    def area(self) -> float:
        return pi * (self.raio ** 2)



        