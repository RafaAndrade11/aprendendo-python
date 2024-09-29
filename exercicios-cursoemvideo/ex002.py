#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Digite seu nome: ')
print ('Seja bem-vindo(a), {}!'.format(nome))

# Utilizando o {} dentro de uma String com aspas simples, podemos utilizar o metodo .format
# para incluir a variável, assim podemos continuar o texto normalmente.