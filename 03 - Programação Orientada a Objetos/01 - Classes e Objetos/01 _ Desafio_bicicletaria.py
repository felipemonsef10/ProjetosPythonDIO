class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def correr(self):
        print('VRUMMMM!')

    def buzinar(self):
        print('BIBI!')

    def parar(self):
        print('STOOOPP!')
        print('Bicicleta parada.')

    # def get_cor(self):
    #     return self.cor

    # def __str__(self):
    #     return f'Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}'

    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join([f"{key}={value}" for key, value in self.__dict__.items()])}'
        # REPRESENTAÇÕES DE CLASSES


b1 = Bicicleta('vermelha', 'caloi', 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)


b2 = Bicicleta('verde', 'monark', 2000, 189)
b2.buzinar()    # Bicicleta.buzinar(b2)
# print(b2.get_cor())
# print(b2.cor)
print(b2)
