from datetime import date


class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nasimento = ano_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _ano_atual = date.today().year
        return _ano_atual - self._ano_nasimento

    # def get_nome(self):
    #     return self._nome
    #
    # def get_idade(self):
    #     return date.today().year - self._ano_nasimento


pessoa = Pessoa('Felipe', 2005)
print(f'Nome: {pessoa.nome} \tIdade:{pessoa.idade}')
# print(f'Nome: {pessoa.get_nome()} \tIdade:{pessoa.get_idade()}')
