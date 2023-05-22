from funcoes import *

while True:
    opcao = menu()
    if opcao == '1':
        cria_usuario()
    if opcao == '2':
        deu_certo = cria_conta(nmr_conta)
        if deu_certo:
            print('CONTA CRIADA COM SUCESSO!')
            nmr_conta += 1
        else:
            print('CPF NÃO POSSUI CADASTRO!')
    if opcao == '3':
        cpf = str(input('Cpf: '))
        valor = float(input('VALOR DE DEPÓSITO: R$'))
        fazer_deposito(cpf, valor)
    if opcao == '4':
        cpf = str(input('Cpf: '))
        valor = float(input('VALOR DE SAQUE: R$'))
        fazer_saque(cpf, valor)
    if opcao == '5':
        cpf = str(input('Cpf: '))
        exibir_extrato(cpf)
    if opcao == '6':
        lista_contas()
