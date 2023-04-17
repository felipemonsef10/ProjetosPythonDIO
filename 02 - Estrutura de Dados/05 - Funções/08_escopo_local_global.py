salario = 2000


def salario_bonus(bonus, lista):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f'lista auxiliar: {lista_aux}')

    salario += bonus
    return salario


lista = [1]
salario_mais_bonus = salario_bonus(500, lista)
print(salario_mais_bonus)
print(lista)
