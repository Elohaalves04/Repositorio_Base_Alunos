print('SISTEMA DE PROVAS')

num = float(input('Quantas provas o aluno(a) realizou? '))
contador = 1
soma = 0

while contador <= num:
   nota = float(input(f'Qual a nota da prova {contador}: '))
   contador += 1
   soma = soma + nota

media = soma / num
print(f'O aluno obteve a média {media}')