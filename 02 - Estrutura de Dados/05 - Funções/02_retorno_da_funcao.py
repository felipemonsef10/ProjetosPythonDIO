def calcular_total(numeros):
    return sum(numeros)


def antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([1, 3, 4, 10]))
print(antecessor_sucessor(10))
