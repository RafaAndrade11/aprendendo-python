# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import floor

numero = float(input('Digite um número real: '))

print('A porção inteira do seu número é: {}'.format(floor(numero)))