# Crie um programa que receba um número inteiro e dia qual é o dia da semana correspondente a este número
# Os dias são:
# 1 - domingo
# 2 - Segunda
# 3 - Terça
# 4 - Quarta
# 5 - Quinta
# 6 - Sexta
# 7 - Sábado

# OUTPUT ESPERADO

# Digite um número: 1
# Domingo

# Digite um número: 2
# Segunda

# Digite um número: 8
# Número errado

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

num = int(input('Digite um número: '))

if num == 1:
    print('Domingo')

elif num == 2:
    print('Segunda-feira')

elif num == 3: 
    print('terça-feira')

elif num == 4:
    print('Quarta-feira')

elif num == 5:
    print('Quinta-feira')

elif num == 6: 
    print('Sexta-feira')

elif num == 7: 
    print('Sábado')
    
else:
    print('Número errado')