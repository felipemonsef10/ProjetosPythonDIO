# opcao = -1
#
# while opcao != 0:
#     print('[1] Sacar\n[2] Extrato\n[0] Sair\n')
#     opcao = int(input('Sua opção: '))
#
#     if opcao == 1:
#         print('Sacando...')
#     elif opcao == 2:
#         print('Exibindo extrato...')


# while True -> enquanto for verdadeiro

# while True:
#     while True:
#         continuar = str(input('Deseja continuar? ')).upper().strip()
#         if continuar in 'NS':
#             break
#         else:
#             print('Opção inválida')
#     if continuar == 'N':
#         print('FINAL DO PROGRAMA')
#         break

n = 0

while n < 20:
    n += 1
    if n == 12:
        # break     # -> interrompe o laço
        continue    # -> pula a execução
    print(n, end=' ')
