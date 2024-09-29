#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
#de tinta necessária para pintá-la , sabendo que cada litro de tinta pinta uma área de 2m²

largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
area = largura * altura

print('Para pintar a parede serão necessários {} litro(s) de tinta.'.format(area/2))
