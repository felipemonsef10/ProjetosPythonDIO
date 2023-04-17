# texto = str(input('Digite um texto: '))]
texto = 'OPA'
vogais = 'AEIOU'

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in vogais:
        print(f'"{letra.upper()}"', 'está entre as vogais "AEIOU".')
# else:
#     print()     # adiciona uma quebra de linha
#     print('Executa no final do laço.')


# Exemplo utilizando a função built-in range
for numero in range(0, 51,5):
    print(numero, end=' ')
