"""
Crie um programa que defina a classe "carro"
com um construtor que recebe dois parâmetros,
a cor e a marca do carro.
O programa deve criar duas instâncias da classe "Carro", "c1", "c2", com diferentes
valores para os parâmetros cor e marca.
Em seguida, o programa deve imprimir a cor e
a marca de cada um dos carros criados
"""


class Carro:
    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca


c1 = Carro('branco', 'Fiat')
c2 = Carro('preto', 'Ford')
print(f'Carro 1: '
      f'\nCor -> {c1.cor}'
      f'\nMarca -> {c1.marca}')
print()
print(f'Carro 2: '
      f'\nCor -> {c2.cor}'
      f'\nMarca -> '
      f'\n{c2.marca}')
