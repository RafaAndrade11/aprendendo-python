#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Digite o preço do produto: '))

print('O preço do produto com 5% de desconto é: R${}'.format(preco-(preco*0.05)))