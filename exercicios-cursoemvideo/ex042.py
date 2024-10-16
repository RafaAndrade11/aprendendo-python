'''
Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes
'''

reta1 = float(input('Digite o comprimento da primera reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    if reta1 == reta2 and reta2 == reta3:
        print('Este é um triângulo equilátero!')
    elif (reta1 == reta2 and reta1 != reta3) or (reta2 == reta3 and reta2 != reta1) or (reta3 == reta1 and reta3 != reta2):
        print('Este é um triângulo isósceles!')
    else:
        print('Este é um triângulo escaleno!')
else:
    print('Os segmentos acima não formam um triângulo.')
    
    