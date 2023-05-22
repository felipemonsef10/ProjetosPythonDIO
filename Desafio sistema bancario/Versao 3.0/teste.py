valor = 1000.123

teste = f'{"> EXTRATO <".center(30, "=")}' \
        f'\nSALDO: R${valor:,.2f}\n\n'


valor2 = 124124.51
valor3 = 124124.124124

teste += f'SAQUE: R${valor2:,.2f}\n'
teste += f'DEPOSITO: R${valor3:,.2f}\n'

print(teste)
