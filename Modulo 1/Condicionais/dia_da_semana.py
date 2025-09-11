from colorama import init, Fore
init(autoreset=True)


numero = int(input('Digite um número: '))

if numero == 1: 
    print(Fore.RED+'domingo')

elif numero == 2: 
    print(Fore.BLUE+'Segunda-feira')

elif numero == 3:
    print(Fore.LIGHTGREEN_EX+'Terça-feira')

elif numero == 4:
    print(Fore.YELLOW+'Quarta-feira')

elif numero == 5:
    print(Fore.LIGHTCYAN_EX+'Quinta-feira')

elif numero == 6:
    print(Fore.LIGHTYELLOW_EX+'Sexta-feira')

elif numero == 7:
    print(Fore.LIGHTMAGENTA_EX+'Sábado')

else: 
    print('número errado!')