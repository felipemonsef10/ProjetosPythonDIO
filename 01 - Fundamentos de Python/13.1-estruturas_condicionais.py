MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade_usuario = int(input('Informe a sua idade: '))

# if idade_usuario >= 18:
#     print('Maior de idade, pode tirar a CNH.')
#
# if idade_usuario < 18:
#     print('Você não é maior de idade, ainda não pode tirar a CNH.')


# if idade_usuario >= 18:
#     print('Maior de idade, pode tirar a CNH.')
# else:
#     print('Você não é maior de idade, não pode tirar CNH.')


if idade_usuario >= 18:
    print('Maior de idade, pode tirar a CNH.')
elif idade_usuario == IDADE_ESPECIAL:
    print(f'Menor de idade, não pode tirar a CNH, porém, com {idade_usuario} anos você pode fazer a aula teórica.')
else:
    print('Você não é maior de idade, não pode tirar CNH.')
