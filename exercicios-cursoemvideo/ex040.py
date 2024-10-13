'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- média abaixo de 5.0: reprovado
- média entre 5.0 e 6,9: recuperação
- média 7.0 ou superior: aprovado
'''

primeira_nota = float(input('Digite sua primeira nota:'))
segunda_nota = float(input('Digite sua segunda nota: '))
media = (primeira_nota + segunda_nota) / 2

if media < 5:
    print('Reprovado!')
elif media >= 5 and media <= 6.9:
    print('Recuperação!')
else:
    print('Aprovado!')