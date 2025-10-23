# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|',40*'-','|')
print('|',15*'-', 'CADASTRO',15*'-','|')
print('|',40*'-','|')
nome = input('| Nome: ')
input('| Idade: ')
email = input('| Email: ')
input('| Senha: ')
print( )
print('|',40*'-','|')
print('|',10*'-','USUÁRIO CADASTRADO',10*'-','|')
print(f'| Seja Bem vindo(a) {nome}')
print(f'| Email: {email}')
print('|',40*'-','|')