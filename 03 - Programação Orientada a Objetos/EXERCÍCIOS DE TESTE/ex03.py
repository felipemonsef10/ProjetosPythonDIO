"""
Crie um programa que defina a classe "Aluno"
com um construtor que recebe três parâmetros,
o nome, a idade e a nota do aluno.
O programa deve criar duas instâncias da classe
"Aluno", "a1" e "a2", com diferentes valores para
os parâmetros nome, idade e nota.
Em seguida, o programa deve imprimir o nome,
a idade e a nota de cada um dos alunos criados.
E por último, calcular e imprimir a média das
notas dos dois alunos criados.
"""


class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota


def media_notas(n1, n2):
    media = (n1 + n2) / 2
    return media


a1 = Aluno('Felipe', 17, 10)
a2 = Aluno('João', 20, 9.5)

print(f'Aluno 1: '
      f'\nNome -> {a1.nome}'
      f'\nIdade -> {a1.idade}'
      f'\nNota -> {a1.nota}')
print()
print(f'Aluno 2: '
      f'\nNome -> {a2.nome}'
      f'\nIdade -> {a2.idade}'
      f'\nNota -> {a2.nota}')
print()
print(f'A média das notas de {a1.nome} e {a2.nome} é: {media_notas(a1.nota, a2.nota):.2f} pts.')
