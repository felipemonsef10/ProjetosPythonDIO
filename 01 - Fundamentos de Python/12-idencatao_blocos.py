def sacar(valor):
    saldo = 500     # Identado dentro da função sacar

    if saldo >= valor:  # Identado dentro da função sacar
        print('Valor sacado com sucesso.')  # Identado dentro do if
        print('Favor retirar no caixa.')    # Identado dentro do if
    else:
        print('Não foi possível realizar a tranzação.')

    print('Obrigado por ser nosso cliente, bom dia.')


def depositar(valor):
    saldo = 500
    saldo += valor
    print(f'Foram depositados R${valor} à sua conta.')
    print(f'O seu novo saldo é de R${saldo}.')


# sacar(400)
# depositar(1000)
