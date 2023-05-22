contas = []


class Conta:
    def __init__(self, cpf):
        self._cpf = cpf
        self._contas = []
        self._saldo = 0
        self.valor_limite_saque = 1500
        self.nmr_limite_saque = 5
        self._extrato = f'{"> EXTRATO <".center(30, "=")}\n\n'

    @property
    def cpf(self):
        return self._cpf

    @property
    def contas(self):
        return self._contas

    def cria_conta(self, conta):
        self._contas.append(conta)

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self._saldo += valor_deposito
            print('DEPÓSITO REALIZADO COM SUCESSO!')
            self._extrato += f'DEPÓSITO: \tR${valor_deposito:,.2f}\n'
        else:
            print('VALOR INVÁLIDO!')

    def sacar(self, valor_saque):
        if valor_saque > 0:
            if self._saldo < valor_saque:
                print('SALDO INDISPONÍVEL!')
                print(f'SALDO: R${self._saldo:.2f}')
            elif valor_saque > self.valor_limite_saque:
                print('VALOR LIMITE DE SAQUE ATINGIDO!')
                print(f'SALDO: R${self._saldo:.2f}')
            elif self.nmr_limite_saque == 0:
                print('LIMITE DE SAQUES ATINGIDOS!')
            elif self._saldo >= valor_saque:
                self.valor_limite_saque -= valor_saque
                self.nmr_limite_saque -= 1
                self._saldo -= valor_saque
                print('SAQUE EFETUADO COM SUCESSO!')
                print(f'SALDO: R${self._saldo:.2f}')
                self._extrato += f'SAQUE: \t\tR${valor_saque:,.2f}\n'
        else:
            print('VALOR INVÁLIDO!')

    @property
    def extrato(self):
        return self._extrato
