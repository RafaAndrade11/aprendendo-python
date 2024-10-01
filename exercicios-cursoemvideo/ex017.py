# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa
from math import sqrt

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)

print('O valor da hipotenusa é: {:.1f}'.format(sqrt(hipotenusa)))
