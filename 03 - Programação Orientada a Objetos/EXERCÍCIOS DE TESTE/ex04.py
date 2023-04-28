# Projeto de conta bancária
# Atributos: nome, saldo
# Métodos: mostrar saldo, sacar, depositar

# Adicionar novas funções:
# 1 - Histórico de depósito e saque
# 2 - Taxas para saque
# 3 - Limite o saque após sacar o valor X
# 4 - Transferência entre contas

class ContaBancaria:

    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self._saques_depositos = []
        self._taxa_saque = 1.5

    def mostrar_saldo(self):
        print('*' * 40)
        print(f'O seu saldo é de R${self.saldo:.2f}')

    def depositar(self, valor_deposito):
        print('=' * 40)
        print(f'DEPÓSITO DE R${valor_deposito:.2f}')
        print('-' * 30)
        self._saques_depositos.append(valor_deposito)
        self.saldo += valor_deposito
        print('DEPÓSITO EFETUADO COM SUCESSO!')

    def sacar(self, valor_saque):
        print('=' * 40)
        print(f'SAQUE DE R${valor_saque:.2f}')
        if (valor_saque * (1 + self._taxa_saque / 100)) > self.saldo:
            print('-' * 30)
            print('ERRO! VOCÊ NÃO POSSUI SALDO SUFICIENTE PARA O SAQUE!')
        else:
            print('-' * 30)
            print(f'Taxa: R${valor_saque * self._taxa_saque / 100:.2f}\t(+{self._taxa_saque}%)')
            valor_saque *= 1 + (self._taxa_saque / 100)
            self._saques_depositos.append(-valor_saque)
            self.saldo -= valor_saque
            print('SAQUE EFETUADO COM SUCESSO!')

    def visualizar_extrato(self):
        print('*' * 40)
        print('EXTRATO DA CONTA:')
        print('-' * 30)
        for saque_deposito in self._saques_depositos:
            if saque_deposito < 0:
                saque_deposito *= -1
                print(f'SAQUE: \t\tR${saque_deposito:.2f}  \t(+1.5%)')
            else:
                print(f'DEPÓSITO: \tR${saque_deposito:.2f}')
        print(f'SALDO: \t\tR${self.saldo:.2f}')
        print('*' * 40)


conta1 = ContaBancaria('Felipe', 200)
conta1.sacar(200)
conta1.depositar(10)
conta1.sacar(200)
conta1.depositar(500)
conta1.sacar(507)

conta1.visualizar_extrato()
