from random import randint

print(25*'-')
print('| TENTE ADIVINHAR O NÚMERO')
print(25*'-')

numero_aleatorio = randint(1,10)
num = int(input('| Tente adividinhar! Digite um número: '))
num_certo = 7

while num != num_certo: 
   print('| Tente novamente!!!')
   numero = int(input('| Digite o número: '))

print('| Você acertou :)')   