# Projeto de conta bancária
# Atributos: nome, saldo
# Métodos: mostrar saldo, sacar, depositar

class ContaBancaria:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f'O seu saldo é de R${self.saldo:.2f}')

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        print('DEPÓSITO EFETUADO COM SUCESSO!')

    def sacar(self, valor_saque):
        if valor_saque > self.saldo:
            print('ERRO! VOCÊ NÃO POSSUI SALDO SUFICIENTE PARA O SAQUE!')
        else:
            self.saldo -= valor_saque
            print('SAQUE EFETUADO COM SUCESSO!')


conta1 = ContaBancaria('Felipe', 500)
conta1.mostrar_saldo()
conta1.depositar(400)
conta1.mostrar_saldo()
conta1.sacar(200)
conta1.mostrar_saldo()
conta1.sacar(1000)
