# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite o nome completo: ')).strip()

if 'Silva' in nome:
    print('Contém Silva!')
else:
    print('Não contém Silva!')