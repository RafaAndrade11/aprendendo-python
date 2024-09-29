#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possiveis sobre ele

entrada = input('Digite algo: ')
print('O que foi digitado: {}'.format(entrada))
print('Tipo primitivo: {}'.format(type(entrada)))
print('É alpha numérico? {}'.format(entrada.isalnum()))
print('É alpha? {}'.format(entrada.isalpha()))
print('É numérico? {}'.format(entrada.isnumeric()))
print('É decimal? {}'.format(entrada.isdecimal()))
print('Só possui letras minúsculas? {}'.format(entrada.islower()))
print('Só possui letras maiúsculas? {}'.format(entrada.isupper()))

