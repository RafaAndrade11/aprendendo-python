#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = int(input('Digite um valor em metros: '))

print('Valor em centímetros: {} \n '
      'Valor em milímetros: {}'
      .format(valor * 100, valor * 1000))