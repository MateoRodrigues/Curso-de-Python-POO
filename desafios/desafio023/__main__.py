from poligono import Quadrado, Circulo
from rich import inspect, print
def main():
    # Área do círculo
    c = Circulo(2)
    print(f' {c.__class__.__name__.capitalize().center(30,'=')} ')
    print(f'Área = {c.area():.2f}')
    print(f'Perímetro = {c.perimetro():.2f}')
    # Área do quadrado
    q = Quadrado(3)
    print(f' {q.__class__.__name__.capitalize().center(30,'=')} ')
    print(f'Área = {q.area():.2f}')
    print(f'Perímetro = {q.perimetro():.2f}')
    
    
if __name__ == '__main__':
    main()