modelo = input('Qual foi o modelo do carro alugado? ')
dias = int(input('Por quantos dias o carro foi alugado: '))
km = float(input('Quantos KM o carro rodou: '))

if modelo == 'onix':
    valor=50

elif modelo == 'kwid':
    valor=60

elif modelo == 'argo':
    valor=100

else: 
    valor = 150

valor_dias= (dias*valor)
valor_km= (km*0.15)
valor_total= (valor_dias+valor_km)
print(f'Você andou {km} KM por {dias} dias, então o preço á pagar é: {valor_total} ')