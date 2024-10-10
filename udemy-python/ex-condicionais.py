primeiro_valor = input('Digite um valor inteiro: ')
segundo_valor = input('Digite outro valor inteiro: ')

#resultados se o usuário digitar números inteiros somente

if primeiro_valor > segundo_valor:
    print('O {} é maior que o {}.'.format(primeiro_valor, segundo_valor))
elif segundo_valor > primeiro_valor:
    print('O {} é maior que o {}.'.format(segundo_valor, primeiro_valor))
else:
    print('Os valores são iguais!') 

if 1 and 1:
    print(True and 1 and False)

    