from conta_banco import *
from pessoa import *


def menu():
    print(' MENU '.center(32, '='))
    print('[1] -> Criar Usuário\n'
          '[2] -> Criar Conta\n'
          '[3] -> Depositar\n'
          '[4] -> Sacar\n'
          '[5] -> Exibir Extrato\n'
          '[6] -> Listar Contas\n'
          '[0] -> Sair do Sistema')
    print('=' * 32)
    return str(input('Opção usuário: '))


def cria_usuario():
    nome = str(input('Nome: ')).title()
    cpf = str(input('Cpf: '))
    ano_nascimento = int(input('Ano de nascimento: '))

    if len(users) == 0:
        usuario = Usuario(nome, cpf, ano_nascimento)
        users.append(usuario)
        print('CLIENTE CADASTRADO COM SUCESSO!')

    else:
        cpfs = [dado.cpf for dado in users]
        if cpf in cpfs:
            print('CPF JÁ CADASTRADO!')
        else:
            usuario = Usuario(nome, cpf, ano_nascimento)
            users.append(usuario)
            print('CLIENTE CADASTRADO COM SUCESSO!')


nmr_conta = 1


def cria_conta(nmr_conta):
    cpfs_users = [dados.cpf for dados in users]
    cpfs_contas = [dados.cpf for dados in contas]

    cpf = str(input('Cpf: '))
    if (len(cpfs_users) == 0) or (cpf not in cpfs_users):
        return False
    else:
        if cpf in cpfs_contas:
            for conta in contas:
                if cpf == conta.cpf:
                    conta.cria_conta(nmr_conta)
        else:
            conta_criada = Conta(cpf)
            conta_criada.cria_conta(nmr_conta)
            contas.append(conta_criada)

        # for conta in contas:
        #     print(conta.cpf, conta.contas)

        return True


def fazer_deposito(cpf, valor_deposito):
    cpfs_users = [dados.cpf for dados in users]
    cpfs_contas = [dados.cpf for dados in contas]

    if (len(cpfs_users) == 0) or (cpf not in cpfs_users):
        print('CPF NÃO POSSUI CADASTRO!')
    elif (len(cpfs_contas) == 0) or cpf not in cpfs_contas:
        print('CPF NÃO POSSUI CONTA!')
    else:
        for conta in contas:
            if cpf == conta.cpf:
                conta.depositar(valor_deposito)

    for conta in contas:
        print(f'{conta.cpf}: {conta.contas}, {conta.saldo}')


def fazer_saque(cpf, valor_saque):
    cpfs_users = [dados.cpf for dados in users]
    cpfs_contas = [dados.cpf for dados in contas]

    if (len(cpfs_users) == 0) or (cpf not in cpfs_users):
        print('CPF NÃO POSSUI CADASTRO!')
    elif (len(cpfs_contas) == 0) or (cpf not in cpfs_contas):
        print('CPF NÃO POSSUI CONTA!')
    else:
        for conta in contas:
            if cpf == conta.cpf:
                conta.sacar(valor_saque)


def exibir_extrato(cpf):
    cpfs_users = [dados.cpf for dados in users]
    cpfs_contas = [dados.cpf for dados in contas]

    if (len(cpfs_users) == 0) or (cpf not in cpfs_users):
        print('CPF NÃO POSSUI CADASTRO!')
    elif (len(cpfs_contas) == 0) or cpf not in cpfs_contas:
        print('CPF NÃO POSSUI CONTA!')
    else:
        for conta in contas:
            if cpf == conta.cpf:
                print(conta.extrato)
                print(f'SALDO: \t\tR${conta.saldo:,.2f}')


def lista_contas():
    print('> CONTAS <'.center(30, '='))
    if len(users) == 0:
        print('0 USUÁRIOS CADASTRADOS!\n')
    elif len(contas) == 0:
        print('0 CONTAS CRIADAS!\n')
    else:
        for conta in contas:
            for usuario in users:
                if conta.cpf == usuario.cpf:
                    print(f'AGÊNCIA:     0001\n'
                          f'CONTAS:      {conta.contas}\n'
                          f'TITULAR:     {usuario.nome}\n\n'
                          f'{"=" * 30}')
