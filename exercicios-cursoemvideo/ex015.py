# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorrido = float(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Digite quantos dias foram alugados: '))

diaria = (dias * 60) + (km_percorrido * 0.15)

print('O preço a pagar será: R${:.2f}.'.format(diaria))