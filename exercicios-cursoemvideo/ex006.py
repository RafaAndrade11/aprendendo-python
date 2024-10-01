#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Digite um número: '))
print ('Número escolhido: {} \n Dobro: {} \n Triplo: {} \n Raíz Quadrada: {}'
       .format(numero, (numero * 2), (numero * 3), (numero ** (1/2))))