print(30*'-')
print('| LISTA DE FILMES')
print(30*'-')

contador = 1
print('| Adicione três filmes á sua playlist...')
lista = []

while contador <= 3:
    filmes = input(f'| Digite o nome do {contador} filme: ')
    contador += 1
    lista.append(filmes)

print(filmes)

