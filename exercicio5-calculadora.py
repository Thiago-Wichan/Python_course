while True:
    
    numero_1 = input('Digite um número: ')
    operador = input('Digite um operador: ')
    numero_2 = input('Digite o segundo número: ')

    numeros_convertidos = None
    operadores_validos = '+-*/'
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_convertidos = True

    except:
        numeros_convertidos = None

    if numeros_convertidos is None:
        print('Digite números válidos')
        continue
    if operador not in operadores_validos:
        print('Digite um operador válido')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador')   
        continue
    print('Realizando sua operação:')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float+num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float-num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float/num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float*num_2_float)

    sair = input('Deseja sair? ').lower().startswith('s')
    if sair is False:
        print('Realize a próxima operação:')
    if sair:
        print('Você saiu.')
        break