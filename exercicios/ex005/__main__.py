from classesex005 import Aluno, Professor, Funcionario

def main():
    a1 = Aluno('Gabriel', 12, 'Programação', 'A')
    a1.fazer_aniversario()
    p1 = Professor('Samuel', 29, 'Biologia', 'Mestrado')
    p1.fazer_aniversario()
    f1 = Funcionario('Cláudia', 30, 'Secretária', 'Secretaria')
    a1.fazer_matricula()
    p1.dar_aula()
    f1.bater_ponto()

if __name__ == '__main__':
    main()