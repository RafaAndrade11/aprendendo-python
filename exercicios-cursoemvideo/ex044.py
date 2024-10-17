''' Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros '''

valor_original = float(input('Digite o valor original do produto: '))
print('FORMAS DE PAGAMENTO: 1 - À VISTA (DINHEIRO OU CHEQUE) / 2 - 2X NO CARTÃO / 3 - 3X OU MAIS NO CARTÃO')
forma_de_pagamento = int(input('Digite o número correspondente a sua forma de pagamento [1, 2 ou 3]: '))

if forma_de_pagamento == 1:
    escolha = int(input('Digite 1 para à vista no dinheiro e 2 para à vista no cheque: '))
    if escolha == 1:
        print(f'O valor a ser pago será: R${valor_original - (valor_original * 0.10)}')
    else:
        print(f'O valor a ser pago será: R${valor_original - (valor_original * 0.05)}')
elif forma_de_pagamento == 2:
    print(f'O valor a ser pago será: 2 x de R${valor_original / 2}')
else:
    quantas_vezes = int(input('Digite em quantas vezes deseja parcelar: '))
    valor_mensal = (valor_original + (valor_original * 0.20)) / quantas_vezes
    print(f'O valor a ser pago será de: {quantas_vezes} x de R${valor_mensal}')