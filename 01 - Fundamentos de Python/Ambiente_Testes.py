n_casos = int(input())

for caso in range(n_casos):
    a, b = map(str, input().split())
    if b == a[-len(b):]:
        print('encaixa')
    else:
        print('nao encaixa')
