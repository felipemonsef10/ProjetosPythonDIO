menu = """==========================
    [1] -> Depositar
    [2] -> Sacar
    [3] -> Extrato
    [0] -> Sair
=========================="""

saldo = 0
saque_diario = 0
extrato = '====== EXTRATO ======\n'
limite_saque = 0


while True:
    print(menu)
    opcao_usuario = str(input('Sua opção: ')).strip()

    if opcao_usuario == '1':
        valor_deposito = float(input('Valor de depósito: R$'))
        if valor_deposito < 0:
            print('ERRO! Valor inválido.')
        else:
            saldo += valor_deposito
            print(f'R${valor_deposito:.2f} depositados com sucesso!')
            extrato += f'Depósito: R${valor_deposito:.2f}\n'

    if opcao_usuario == '2':
        valor_saque = float(input('Valor saque: R$'))
        if valor_saque <= saldo:
            if saque_diario < 1500 and limite_saque < 3:
                saldo -= valor_saque
                limite_saque += 1
                saque_diario += valor_saque
                print('Saque efetuado com sucesso.')
                extrato += f'Saque: R${valor_saque:.2f}\n'
            else:
                print('ERRO! Limite de saque excedido.')

        elif valor_saque > saldo:
            print('ERRO! Saldo insuficiente.')

        elif valor_saque < 0:
            print('ERRO! Valor inválido.')

    if opcao_usuario == '3':
        extrato += f'\nSaldo: R${saldo:.2f}'
        print(extrato)
        print('=' * 21)
    if opcao_usuario == '0':
        break

    if opcao_usuario not in '0123':
        print('OPÇÃO INVÁLIDA')
