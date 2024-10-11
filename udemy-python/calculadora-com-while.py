resp = True

while resp:
    
    numero1 = (input('Digite o primeiro número: '))
    numero2 = (input('Digite o segundo número: '))
    print('SOMA / SUBTRACAO / MULTIPLICACAO / DIVISAO')
    operacao = input('Digite a operação desejada: ')
    
    numeros_validos = True
    
    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None
        print('Um ou ambos os valores são inválidos! Tente novamente!')
        continue

    if (operacao == 'SOMA'):
        print('A soma de {} + {} = {}'.format(numero1_float, numero2_float, numero1_float + numero2_float))
    elif (operacao == 'SUBTRACAO'):
        print('A subtracao de {} - {} = {}'.format(numero1_float, numero2_float, numero1_float - numero2_float))
    elif (operacao == 'MULTIPLICACAO'):
        print('A multiplicacao de {} * {} = {}'.format(numero1_float, numero2_float, numero1_float * numero2_float))
    elif (operacao == 'DIVISAO'):
        print('A divisão de {} / {} = {}'.format(numero1_float, numero2_float, numero1_float / numero2_float))
    else:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE ESCREVENDO CORRETAMENTE.')

    continuar = input('Digite "SAIR" para sair ou qualquer coisa para continuar: ').lower()
    print (continuar)

    if continuar == 'sair':
        resp = False
        