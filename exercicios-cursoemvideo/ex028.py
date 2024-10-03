# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu.

from random import randint

print('SORTEANDO UM NÚMERO...')

numero = randint(0, 5)
escolha = int(input('Escolha um número de 0 a 5:'))

if numero == escolha:
    print('PARABÉNS, VOCÊ ACERTOU!')
else:
    print('ERROU! O NÚMERO CERTO ERA {}'.format(numero))