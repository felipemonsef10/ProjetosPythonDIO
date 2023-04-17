saldo = 1000
saque = 5000

status = 'Sucesso' if saldo > saque else 'Falha'  # --> estrutura condicional em apenas uma linha

print(f'{status} ao realizar saque.')
