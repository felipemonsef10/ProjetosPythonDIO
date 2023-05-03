from datetime import date
from conta_banco import Conta


class Pessoa:
    def __init__(self, nome, ano_nascimento, cpf):
        ano_nascimento = ano_nascimento.split('-')
        ano_nascimento.reverse()
        self.ano_nascimento = int(ano_nascimento[0])
        self.nome = nome
        self.cpf = cpf
        self.idade = int(date.today().year) - self.ano_nascimento

    # def abrir_nova_conta(self):
