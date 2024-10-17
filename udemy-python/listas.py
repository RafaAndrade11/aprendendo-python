"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Métodos úteis:
append - adiciona um item ao final
insert - adiciona um item no índice escolhido
pop - remove do final ou do índice escolhido
del - apaga um índice
clear - limpa a lista
extend - estende a lista
+ - concatena listas
"""

lista = ['Maria', 'Helena', 'Luiz']
indice = 0

for nome in lista:
    print(nome , "está no índice: " , indice)
    indice = indice + 1