# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Digite a velocidade do carro em Km/H: '))

if (velocidade > 80):
    print('Proibido passar de 80Km/h, você foi multado! Sua multa custará R$7,00 por cada Km acima do limite')
    print('Valor da multa: R${}'.format((velocidade-80)*7))
else:
    print('Parabéns, você está dentro da velocidade permitida!')