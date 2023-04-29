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
        self._saques_depositos_transfer = []
        self._taxa_saque = 1.5
        self._limite_valor_saque = 2000

    def mostrar_saldo(self):
        print('*' * 40)
        print(f'O seu saldo é de R${self.saldo:.2f}')

    def depositar(self, valor_deposito):
        print('=' * 40)
        print(f'DEPÓSITO DE R${valor_deposito:.2f}')
        print('-' * 30)
        self._saques_depositos_transfer.append(valor_deposito)
        self.saldo += valor_deposito
        print('DEPÓSITO EFETUADO COM SUCESSO!')

    def sacar(self, valor_saque):
        print('=' * 40)
        print(f'SAQUE DE R${valor_saque:.2f}')
        print(f'Taxa: R${valor_saque * self._taxa_saque / 100:.2f}\t(+{self._taxa_saque}%)')
        if (valor_saque * (1 + self._taxa_saque / 100)) > self.saldo:
            print('-' * 30)
            print('ERRO! VOCÊ NÃO POSSUI SALDO SUFICIENTE PARA O SAQUE!')
        elif (valor_saque * (1 + self._taxa_saque / 100)) < self.saldo:
            print('-' * 30)
            if self._limite_valor_saque == 0:
                print('ERRO! O VALOR LIMITE DE SAQUE FOI ATINGIDO!')
                print(f'LIMITE DISPONÍVEL: R${self._limite_valor_saque:.2f}')
            elif valor_saque * (1 + (self._taxa_saque / 100)) > self._limite_valor_saque:
                print('ERRO! O VALOR DE SAQUE MAIS A TAXA ULTRAPASSA O VALOR DE LIMITE!')
                print(f'LIMITE DISPONÍVEL: R${self._limite_valor_saque:.2f}')
            else:
                valor_saque *= 1 + (self._taxa_saque / 100)
                self._saques_depositos_transfer.append(-valor_saque)
                self.saldo -= valor_saque
                self._limite_valor_saque -= valor_saque
                print('SAQUE EFETUADO COM SUCESSO!')
                print(f'LIMITE DISPONÍVEL: R${self._limite_valor_saque:.2f}')

    def visualizar_extrato(self):
        print('*' * 40)
        print('EXTRATO DA CONTA:')
        print('-' * 30)
        for saque_deposito_transf in self._saques_depositos_transfer:
            if saque_deposito_transf is str:
                saque_deposito_transf.replace('t', '')
                print(f'TRASFERÊNCIA: {float(saque_deposito_transf):.2f}')
            else:
                if saque_deposito_transf < 0:
                    saque_deposito_transf *= -1
                    print(f'SAQUE: \t\t\t\t\tR${saque_deposito_transf:.2f}  \t(+1.5%)')
                else:
                    print(f'DEPÓSITO: \t\t\t\tR${saque_deposito_transf:.2f}')
        print(f'\nSALDO: \t\t\t\t\tR${self.saldo:.2f}')
        print(f'LIMITE DISPONÍVEL: \t\tR${self._limite_valor_saque:.2f}')
        print('*' * 40)

    def fazer_transferencia(self, valor_transferencia, conta_destino):
        print(f'VALOR DE TRANSFERÊNCIA: R${valor_transferencia:.2f}')
        if valor_transferencia > self.saldo:
            print('ERRO! SALDO INSUFICIENTE PARA COMPLETAR A TRANSAÇÃO!')
        else:
            print('TRANSFERÊNCIA REALIZADA COM SUCESSO!')
            self.saldo -= valor_transferencia
            conta_destino.depositar(valor_transferencia)
            self._saques_depositos_transfer.append('t' + str(valor_transferencia))


conta1 = ContaBancaria('Felipe', 2000)
conta2 = ContaBancaria('João', 0)
conta1.fazer_transferencia(500, conta2)
