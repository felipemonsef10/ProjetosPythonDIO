conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 3000
saque = 2500
cheque_especial = 400

if conta_normal:
    if saldo > saque:
        print('Saque realizado com sucesso.')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso de cheque especial.')
    else:
        print('Saque negado. Saldo insuficiente.')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso.')
    else:
        print('Saque negado. Saldo insuficiente.')
elif conta_especial:
    print('Conta especial selecionada.')
else:
    print('Não foi possível reconhecer o seu tipo de conta, entre em contato com o seu gerente.')
