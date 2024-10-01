#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

temperatura = int(input('Digite a temperatura em graus Celsius: '))
farenheit = (temperatura * 9/5) + 32

print("{}° = {}F".format(temperatura, farenheit))