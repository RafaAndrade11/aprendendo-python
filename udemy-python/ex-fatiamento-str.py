nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print('Seu nome é: {}'.format(nome))
    print('Seu nome invertido é {}:'.format(nome[::-1]))

    if ' ' in nome:
        print('Seu nome contém espaços!')
    else:
        print('Seu nome não contém espaços!')

    print('Seu nome contém {} letras'.format(len(nome)))
    print('A primeira letra do seu nome é: {}'.format(nome[0]))
    print('A última letra do seu nome é: {}'.format(nome[-1]))
else:
    print('Desculpe, você deixou campos vazios.')