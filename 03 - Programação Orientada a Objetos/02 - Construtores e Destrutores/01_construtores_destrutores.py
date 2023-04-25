class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print('Removendo a instância da classe.')

    def falar(self):
        print('AUAUAU')


def criar_cachorro():
    c = Cachorro('Rock', 'Malhado', False)
    print(c.nome)


cachorro1 = Cachorro('Salcicha', 'Preto')
cachorro1.falar()

print('OLA, MUNDO')

del cachorro1   # FORÇA A DESTRUIÇÃO

print('OLA, MUNDO')
print('OLA, MUNDO')
print('OLA, MUNDO')

# criar_cachorro()
