class Conta:
    def __init__(self, cliente, data_nascimento_cliente, cpf_cliente):
        self.nome_cliente = cliente
        self.data_nascimento = data_nascimento_cliente
        self.cpf = cpf_cliente
        self._saldo = 0

    def depositar(self, cpf, valor_deposito):
        self._saldo = valor_deposito

