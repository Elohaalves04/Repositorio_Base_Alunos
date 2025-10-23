from colorama import init, Fore
init(autoreset=True)

print('|',35*'_')
print('|')
print('| SISTEMA DE PROVAS')
print('|',35*'_')
print('|')
Name = input('| Nome do aluno: ')
nota1 = float(input('| Nota da primeira nota da prova: '))
nota2 = float(input('| Nota da seguna nota da prova: '))
nota3 = float(input('| Nota da terceira nota da prova: '))
Média = round((nota1+nota2+nota3)/3,1)
print('|',35*'_')
if Média >= 5:
    print(Fore.GREEN+f'{Name}... Você foi Aprovado(a)!')
else:
    print(Fore.RED+f'{Name}... Você foi Reprovado(a)!')  
