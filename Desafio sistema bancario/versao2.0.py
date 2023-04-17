saldo = 0
saque = 0
deposito = 0
limite_saque_diario = 0
numero_limite_saques = 3
extrato = ''


def linha():
    print('=' * 40)


def opcoes():
    linha()
    print(f'{"OPÇÕES":>20}')
    linha()
    print('''    [1] -> Depositar
    [2] -> Sacar
    [3] -> Visualizar extrato
    [4] -> Criar usuário
    [5] -> Criar conta corrente
    [0] -> Sair do sistma''')
    linha()


def exibir_extrato(valor_saque=0, valor_deposito=0):
    global extrato
    if valor_saque != 0:
        extrato += f'\nSaque: R${valor_saque:.2f}'
    if valor_deposito != 0:
        extrato += f'\nDepósito: R${valor_deposito:.2f}'
    linha()
    print(f'{"EXTRATO":>20}')
    print(extrato)
    print(f'\nSaldo: R${saldo:.2f}')


def opcao_usuario(opcao):
    return opcao


def depositar(quantia):
    global saldo
    global extrato
    saldo += quantia
    return quantia


def sacar(valor_saque, saldo_disponivel, qtd_saque_limite, limite_saque=1500):
    global limite_saque_diario
    global numero_limite_saques
    global saldo
    global extrato

    if valor_saque > saldo_disponivel:
        linha()
        print('ERRO! VOCÊ NÃO POSSUI SALDO SUFICIENTE PARA REALIZAR A OPERAÇÃO!')
    elif valor_saque > limite_saque or limite_saque_diario > limite_saque:
        linha()
        print('ERRO! VOCÊ ATINGIU O VALOR LIMITE DE SAQUE DIÁRIO!')
    elif qtd_saque_limite == 0:
        linha()
        print('ERRO! VOCÊ ATINGIU O NÚMERO MÁXIMO DE OPERAÇÕES DIÁRIAS!')
    else:
        saldo -= valor_saque
        limite_saque_diario += valor_saque
        numero_limite_saques -= 1
        return valor_saque


while True:
    while True:
        opcoes()
        escolha_usuario = opcao_usuario(input('Digite sua opção: '))
        if escolha_usuario not in '012345':
            linha()
            print('OPÇÃO INVÁLIDA!')
        else:
            break

    if escolha_usuario == '1':
        linha()
        deposito += depositar(float(input('Valor de depósito: R$')))
        print('DEPÓSITO EFETUADO!')

    if escolha_usuario == '2':
        linha()
        saque += sacar(float(input('Valor de saque: R$')), saldo, numero_limite_saques)

    if escolha_usuario == '3':
        exibir_extrato(saque, deposito)
        saque = 0
        deposito = 0
