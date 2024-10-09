#Interpolação básica de strings

nome = 'Rafael'
preco = 200.232323
frase = '%s, o preço é: R$%.2f'% (nome, preco)
print (frase)

#Parecido com o format, dessa vez utilizamos o % + a letra do tipo de variável e em seguida declaramos qual variável queremos inserir