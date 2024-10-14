"""
Faça um jogo para o usuário adivinhar qual a palavra secreta. 
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- A letra que o usuário digitar, você vai conferir se a letra digitada está na palavra secreta.
- Se a letra estiver na palavra secreta; exiba a letra;
- Se a letra não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
deseja_continuar = True
palavra_secreta = 'arrascaeta'
letras_acertadas = ""
numero_tentativas = 0

while deseja_continuar:
    while True:
        letra_escolhida = input('Digite uma letra: ')
        numero_tentativas += 1
        
        if len(letra_escolhida) > 1:
            print('Digite apenas uma letra.')
            continue
        
        if letra_escolhida in palavra_secreta:
            letras_acertadas += letra_escolhida
            
        for letra_escolhida in palavra_secreta:
            if letra_escolhida in letras_acertadas:
                print(letra_escolhida)
            else:
                print('*')

sair = input('Digite "SAIR" para sair ou qualquer coisa para continuar: ').lower()

if sair == 'sair':
    deseja_continuar = False



