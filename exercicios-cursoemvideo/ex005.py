#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

numero = int(input('Digite um número: '))
print('Número escolhido: {} \n Sucessor: {} \n Antecessor: {}'.format(numero, int(numero + 1), int(numero - 1)))