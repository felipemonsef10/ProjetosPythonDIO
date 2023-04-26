class Estudante:
    escola = 'DIO'  # VARIÁVEL DE CLASSE

    def __init__(self, nome, matricula):
        self.nome = nome    # VARIÁVEL DE INSTÂNCIA
        self.matricula = matricula  # VARIÁVEL DE INSTÂNCIA

    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno1 = Estudante('Felipe', 1)
aluno2 = Estudante('Joana', 2)
mostrar_valores(aluno1, aluno2)

# Estudante.escola = 'Python'     # VARIÁVEL DE CLASSE
# aluno1.matricula = 3    # VARIÁVEL DE INSTÂNCIA

aluno1.escola = 'Python'    # VARIÁVEL DE INSTÂNCIA
aluno3 = Estudante('Pedro', 3)
mostrar_valores(aluno1, aluno2, aluno3)
