# Crie um programa que faça o computador jogar Jokenpô com você.

import random


print('BEM-VINDO(A) AO JOGO JOKENPÔ!')

"""
REGRAS: 
- PAPEL GANHA DE PEDRA
- PEDRA GANHA DE TESOURA
- TESOURA GANHA DE PAPEL
"""

fim = False

while fim == False:
    opcoes_disponiveis = ('PEDRA', 'PAPEL', 'TESOURA')
    escolha_da_maquina = random.rand(opcoes_disponiveis)
    sua_escolha = input('Digite sua escolha, pode ser PEDRA, PAPEL ou TESOURA: ')
    
    print (f'A escolha da máquina foi: {escolha_da_maquina}')
    print (f'Sua escolha foi: {sua_escolha}')
    
    if (sua_escolha == 'PEDRA'):
        ###
    elif (sua_escolha == 'PAPEL'):
        ###
    else (sua_escolha == 'TESOURA'):
   