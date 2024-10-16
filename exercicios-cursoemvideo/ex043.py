''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, e acordo com a tabela abaixo:

- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida '''

peso = float(input('Digite seu peso(kg): '))
altura = float(input('Digite sua altura(m)'))
imc = peso/(altura * altura)

print(imc)