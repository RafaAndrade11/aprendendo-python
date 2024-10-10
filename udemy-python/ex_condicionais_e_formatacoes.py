"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_inteiro = int(input('Digite um número inteiro: '))

if numero_inteiro:
    if numero_inteiro % 2 == 0:
        print('Este número é par!')
    else:
        print('Este número é ímpar')
else:
    print('Você não digitou um número inteiro!')

print ('*' * 20)

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0 - 11, Boa tarde 12 - 17 e Boa noite 18 - 23
"""

hora = int(input('Digite a hora [0 até 23]: '))

if hora >= 0 and hora <= 11:
    print('Bom dia!')
elif hora >= 12 and hora <= 17:
    print('Boa tarde')
else:
    print('Boa noite!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande
"""

primeiro_nome = input('Digite seu primerio nome: ')

if (len(primeiro_nome)) <= 4:
    print('Seu nome é curto!')
elif (len(primeiro_nome)) == 5 or (len(primeiro_nome)) == 6:
    print('Seu nome é normal!')
else:
    print('')

