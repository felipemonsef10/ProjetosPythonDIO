contatos = {
    'pikatofly17@gmail.com': {'nome': 'João', 'telefone': '3333333333'},
    'felipemonsef10@gmail.com': {'nome': 'Felipe', 'telefone': '333333333'},
    'pedrin10@gmail.com': {'nome': 'Pedro', 'telefone': '333333333'},
    'cesinhamg@gmail.com': {'nome': 'César', 'telefone': '33333333'}
}

print(contatos.pop('pikatofly17@gmail.com'))
print(contatos.pop('pedrin10@gmail.com', {}))
print(contatos.pop('pedrin10@gmail.com', 'já foi removido'))
# contatos.pop('pikatofly17@gmail.com')
print(contatos)
