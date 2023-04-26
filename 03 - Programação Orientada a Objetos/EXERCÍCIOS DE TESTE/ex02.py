"""
Crie um programa que defina a classe "Círculo"
com um construtor que recebe um paraâmetro,
o raio do círculo.
O programa deve criar duas instâncias da classe
"Círculo", "c1" e "c2", com diferentes valores para o parâmetro raio.
Em seguida, o programa deve imprimir o raio e a área de cada um dos círculos criados.
"""


class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.area = raio * raio * 3.14


c1 = Circulo(2)
c2 = Circulo(4)
print(f'Raio do círculo 1: {c1.raio}'
      f'\nÁrea do círculo 1: {c1.area}')
print()
print(f'Raio do círculo 2: {c2.raio}'
      f'\nÁrea do círculo 2: {c2.area}')
