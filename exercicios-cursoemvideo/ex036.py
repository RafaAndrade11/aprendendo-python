'''Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado'''

valor_casa = float(input('Digite o valor da casa: '))
salario_comprador = float(input('Digite seu salário: '))
anos_pagamento = float(input('Digite em quantos anos deseja pagar: '))

prestacao_mensal = valor_casa / (anos_pagamento * 12)

if prestacao_mensal > (salario_comprador + (salario_comprador * 0.30)):
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado! O valor da prestação mensal será: R${:.4},00'.format(prestacao_mensal)) 

    

