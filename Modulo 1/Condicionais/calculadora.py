


print('|',30*'_','|')
print('| CALCULADORA')
print('|',30*'_','|')
print('| 1- Soma ')
print('| 2- Subtração ')
print('| 3- Multiplicação ')
print('| 4- Divisão ')
print('|',30*'-',)
opcao = int(input('| Escolha uma das opções: '))
primeiro = int(input('| Digite o primeiro número: '))
segundo = int(input('| Digite o segundo número: '))

if opcao == 1:
   print(f'| O resultado é: {primeiro+segundo}')

elif opcao == 2:
    print(f'| O resultado é: {primeiro-segundo}')

elif opcao == 3: 
    print(f'| O resultado é: {primeiro*segundo}')

elif opcao == 4:
    print(f'| O resultado é: {primeiro/segundo}')

else: 
    print('número errado')



  

