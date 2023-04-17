contatos = {
    'pikatofly17@gmail.com': {'nome': 'João', 'telefone': '3333333333'},
    'felipemonsef10@gmail.com': {'nome': 'Felipe', 'telefone': '333333333'},
    'pedrin10@gmail.com': {'nome': 'Pedro', 'telefone': '333333333'},
    'cesinhamg@gmail.com': {'nome': 'César', 'telefone': '33333333'}
}

for key in contatos:
    print(key, contatos[key])
print()
for k, v in contatos.items():
    print(k, v)
