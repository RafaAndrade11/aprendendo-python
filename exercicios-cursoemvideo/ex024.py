# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome de uma cidade: ')).strip()

if cidade[:5] == 'Santo':
    print('Começa com Santo!')
else:
    print('Não começa com Santo!')