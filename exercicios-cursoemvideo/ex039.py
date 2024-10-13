'''
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''

ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = 2024
idade = ano_atual - ano_nascimento

if idade < 18:
    print('Você ainda irá se alistar ao serviço militar!')
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    print('Já passou seu tempo de alistamento!')