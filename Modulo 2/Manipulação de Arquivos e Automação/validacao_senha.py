import json

with open('senha.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

email = input('Digite seu email: ')
senha = input('Digite sua senha: ')

if email == dados["email"] and senha == dados["senha"]:
    print('Acesso liberado!')

else:
    print('Acesso negado!')
