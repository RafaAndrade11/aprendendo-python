# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras tem ao total (sem considerar espaços)
# - Quantas letras tem no primeiro nome

nome = str(input('Digite seu nome completo: ')).strip() #unificando o nome para tirar os espaços

print('Nome completo com tudo maiúsculo: {}'.format(nome.upper()))
print('Nome completo com tudo minúsculo: {}'.format(nome.lower()))
print('Total de letras sem considerar os espaços: {}'.format(len(nome) - nome.count(' ')))
print('Total de letras no primeiro nome: {}'.format(nome.find(' ')))
