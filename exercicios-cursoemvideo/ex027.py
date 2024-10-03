# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Digite o nome completo: ')).strip()
litaNome = nome.split()

print('Primeiro nome: {}'.format(litaNome[0]))
print('Último nome: {}'.format(litaNome[len(litaNome)-1]))