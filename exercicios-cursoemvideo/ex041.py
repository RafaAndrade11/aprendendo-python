'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 20 anos: sênior
acima de 20: master
'''

ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = 2024
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Mirim!')
elif idade > 9 and idade <= 14:
    print('Infantil!')
elif idade > 14 and idade <= 19:
    print('Júnior!')
elif idade > 19 and idade <= 20:
    print('Sênior!')
else:
    print('Master!')