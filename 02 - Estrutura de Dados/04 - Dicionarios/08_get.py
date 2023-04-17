contatos = {
    'pikatofly17@gmail.com': {'nome': 'João', 'telefone': '3333333333'},
}

print(contatos.get('chave'))
print(contatos.get('chave', {}))
print(contatos.get('pikatofly17@gmail.com', {}))
