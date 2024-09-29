#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
#Considere US$1,00 = R$5,43

valor = float(input('Digite quantos reais tem na carteira: '))

print('Com R${} você pode trocar por US${}.'.format(valor, valor / 5.43))