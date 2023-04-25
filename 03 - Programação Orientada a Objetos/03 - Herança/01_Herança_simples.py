class Veiculo():
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando motor')

    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join([f"{key}={value}" for key, value in self.__dict__.items()])}'


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{"Sim" if self.carregado else "Não"}, estou carregado!')


moto = Motocicleta('preto', 'asd-1234', 2)
# moto.ligar_motor()

carro = Carro('branco', 'xtz-4695', 4)
# carro.ligar_motor()

caminhao = Caminhao('roxo', 'hcz-4795', 8, True)
# caminhao.ligar_motor()
# caminhao.esta_carregado()

print(moto)
print(carro)
print(caminhao)
