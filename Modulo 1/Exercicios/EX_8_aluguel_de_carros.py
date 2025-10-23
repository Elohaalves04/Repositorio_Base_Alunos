# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

dias = int(input('Por quantos dias o carro foi alugado: '))
km = float(input('Quantos KM o carro rodou: '))
total_dias = dias*60
total_km = km*0.15
total_valor = total_dias+total_km
print(f'Você andou {km} KM por {dias} dias, então o preço a pagar é: {total_valor}')