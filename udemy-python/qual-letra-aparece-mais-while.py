#Qual letra aparece mais vezes na frase?

frase = 'O Python é uma linguagem de programação multiparadigma. \
    Python foi criado por Guido van Rossum.'
    
indice = 1
letra_anterior = 'O'

while indice < len(frase):
    letra_atual = frase[indice]
    
    if (frase.count(letra_atual)) > (frase.count(letra_anterior)):
        letra_mais_contada = frase[indice]
    
    letra_atual += 1
    
print('A letra mais contada foi: {}'.format(letra_mais_contada))

#TO DO