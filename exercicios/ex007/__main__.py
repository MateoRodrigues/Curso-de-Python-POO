from classes import Aluno, Professor, Funcionario
from rich.traceback import install
install()
def main():
    a1 = Aluno('Gabriel', 12, 'Programação', 'A')
    a1.fazer_aniversario()
    a1.fazer_matricula()
    a1.estudar()
    p1 = Professor('Samuel', 29, 'Biologia', 'Mestrado')
    p1.fazer_aniversario()
    p1.dar_aula()
    p1.estudar()
    f1 = Funcionario('Cláudia', 30, 'Secretária', 'Secretaria')
    f1.fazer_aniversario()
    f1.bater_ponto()
    f1.estudar()

if __name__ == '__main__':
    main()