users = []


class Usuario:
    def __init__(self, nome, cpf, ano_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def ano_nascimento(self):
        return self._ano_nascimento
