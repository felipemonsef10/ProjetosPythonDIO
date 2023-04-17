usuarios = dict()
cpfs_usuario = dict()
dados_usuarios = dict()
endereco = dict()
saldo = 0
saque = 0
deposito = 0
limite_saque_diario = 0
numero_limite_saques = 3
extrato = ''
cpf_contas = dict()
contas = list()
num_conta = 0


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
    [6] -> Listar contas
    [0] -> Sair do sistma''')
    linha()


def cadastro():
    usuarios['usuarios'] = cpfs_usuario
    dados_usuarios['nome'] = str(input('Nome do usuário: ')).title()
    dados_usuarios['nascimento'] = str(input('Data de nascimento: '))
    while True:
        cpf = str(input('Cpf do usuário: '))
        if cpf in usuarios['usuarios'].keys():
            print('ERRO! CPF JÁ CADASTRADO')
        else:
            break
    endereco['estado'] = str(input('''ENDEREÇO\nEstado(Sigla): ''')).upper()
    endereco['cidade'] = str(input('Cidade: ')).title()
    endereco['bairro'] = str(input('Bairro: ')).title()
    endereco['rua'] = str(input('Rua: ')).title()
    endereco['numero'] = str(input('Número da casa: '))
    dados_usuarios['endereco'] = endereco.copy()
    cpfs_usuario[cpf] = dados_usuarios.copy()
    usuarios['usuarios'] = cpfs_usuario.copy()


def criar_conta():
    global cpf_contas
    global contas
    global num_conta

    while True:
        cpf = str(input('Número do Cpf: '))
        if cpf not in usuarios['usuarios'].keys():
            print('ERRO! CPF INEXISTENTE.')
        else:
            num_conta += 1
            if cpf in cpf_contas.keys():
                cpf_contas[cpf].append(num_conta)
            else:
                cpf_contas[cpf] = contas.copy()
                cpf_contas[cpf].append(num_conta)
            print('CONTA CRIADA COM SUCESSO!')
            break


def mostrar_contas():
    for k, v in cpf_contas.items():
        linha()
        print('Agência:                 0001')
        print(f'Conta corrente:          {v}')
        print('Titular:                ', usuarios['usuarios'][k]['nome'])


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


linha()
print(f'{"PRIMEIRO CADASTRO":>28}')
linha()
cadastro()


while True:
    while True:
        opcoes()
        escolha_usuario = opcao_usuario(input('Digite sua opção: '))
        if escolha_usuario not in '0123456':
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

    if escolha_usuario == '4':
        linha()
        cadastro()

    if escolha_usuario == '5':
        linha()
        criar_conta()

    if escolha_usuario == '6':
        linha()
        mostrar_contas()

    if escolha_usuario == '0':
        break
