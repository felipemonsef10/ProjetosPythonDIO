def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação é = {resultado}')


exibir_resultado(10, 20, somar)
exibir_resultado(10, 20, subtrair)

op = somar

print(op(1, 23))
