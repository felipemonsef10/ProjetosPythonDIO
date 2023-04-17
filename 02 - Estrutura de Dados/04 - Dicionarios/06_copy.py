contatos = {
    'pikatofly17@gmail.com': {'nome': 'João', 'telefone': '3333333333'},
}
print(contatos)
print()

copia = contatos.copy()
copia['pikatofly17@gmail.com'] = {'nome': 'Felipe'}
print(copia)
print()

print(contatos)
