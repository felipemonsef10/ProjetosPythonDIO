from datetime import date


class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, nome):
        idade = date.today().year - ano
        return cls(nome, idade)

    @staticmethod
    def maior_idade(idade):
        return idade >= 18


# p = Pessoa('Felipe', 17)
# print(p.nome, p1.idade)

p = Pessoa.criar_de_data_nascimento(2005, 'Felipe')
print(p.nome, p.idade)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(8))
