nome = 'Felipe'
idade = 17
profissao = 'programador'
linguagem = 'Python'
saldo = 10.23214

dados = {'nome': 'Felipe', 'idade': 17, 'profissao': 'programador', 'linguagem': 'python'}

print('Olá, me chamo %s, tenho %d anos, trabalho de %s e estou estudando %s.' % (nome, idade, profissao, linguagem))
print('Olá, me chamo {}, tenho {} anos, trabalho de {} e estou estudando {}.'.format(nome, idade, profissao, linguagem))
print('Olá, me chamo {1} e tenho {0} anos.'.format(idade, nome))
print('Olá, me chamo {name} e tenho {age} anos.'.format(name=nome, age=idade))
print('Olá, me chamo {nome} e tenho {idade} anos.'.format(nome=nome, idade=idade))
print('Olá, me chamo {nome}, tenho {idade} anos, trabalho de {profissao} e estudo {linguagem}.'.format(**dados))
print(f'Olá, me chamo {nome}, tenho {idade} anos, trabalho de {profissao} e estou estudando {linguagem}.')
print(f'Saldo: {saldo}')
print(f'Saldo: {saldo:.2f}')
print(f'Saldo: {saldo:10.2f}')
