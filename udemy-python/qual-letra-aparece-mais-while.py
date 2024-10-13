#Qual letra aparece mais vezes na frase?

frase = 'O Python é uma linguagem de programação multiparadigma. \
    Python foi criado por Guido van Rossum.'
    
indice = 0
letra_que_mais_apareceu = ''
quantidade_apareceu_mais_vezes = 0

while indice < len(frase):
    letra_atual = frase[indice]
    quantidade_apareceu_mais_vezes_atual = frase.count(letra_atual)
    
    if letra_atual == ' ':
        indice += 1
        continue
   
    if quantidade_apareceu_mais_vezes < quantidade_apareceu_mais_vezes_atual:
        quantidade_apareceu_mais_vezes = quantidade_apareceu_mais_vezes_atual
        letra_que_mais_apareceu = letra_atual
        
    if quantidade_apareceu_mais_vezes == quantidade_apareceu_mais_vezes_atual:
        letras_que_mais_apareceram = '(' + letra_que_mais_apareceu + ') '
    
    indice += 1
    
print('A letra mais contada foi: {}'.format(letras_que_mais_apareceram))