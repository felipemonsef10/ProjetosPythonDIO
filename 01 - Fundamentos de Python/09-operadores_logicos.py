# AND = para ser True tudo tem que ser True
# OR =  para ser True apenas um tem que ser True

print(True and True)
print(True and False and True)
print(False and False)
print(True or True or True)
print(True or False or False)
print(False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True


expressao = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(expressao)

expressoa_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expressoa_2)

condicao_1 = (saldo >= saque and saque <= limite)
condicao_2 = (conta_especial and saldo >= saque)

expressao_3 = condicao_1 or condicao_2
print(expressao_3)
