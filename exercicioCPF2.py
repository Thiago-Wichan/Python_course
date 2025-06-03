# Cálculo do primeiro dígito do CPF #
import sys
import random


for _ in range(100):
    entrada = ''
    for i in range(9):
        entrada += str(random.randint(0,9))

    
    cpf = list(entrada.replace('.', '').replace('-',''))
    cpf_primeiro_digito = cpf[:9]

    multiplicador = 10
    soma = 0
    total = 0

    entrada_sequencial = entrada == entrada[0] * len(entrada)

    if entrada_sequencial:
        print('Você enviou dados sequenciais.')
        sys.exit()

    if len(cpf) != 11 and len(cpf) != 9: 
        print('Digite um CPF válido de 11 caracteres com ponto e dígito ou apenas os 9 primeiros dígitos')
        sys.exit()


    if len(cpf_primeiro_digito) == 11 or len(cpf_primeiro_digito) == 9:
        for numero in cpf_primeiro_digito:
            numero = int(numero)
            soma = (numero * multiplicador)
            multiplicador -= 1
            total += soma    
        
    primeiro_digito = (total * 10 % 11)
    resultado = primeiro_digito if primeiro_digito <= 9 else 0
    #print(f'O primeiro digito de seu CPF deveria ser {resultado}.')

    multiplicador_2 = 11
    soma_2 = 0
    total_2 = 0
    cpf_segundo_digito = list(cpf_primeiro_digito)  
    cpf_segundo_digito.append(resultado)


    for numero_2 in cpf_segundo_digito:
        numero_2 = int(numero_2)
        soma_2 = (numero_2 * multiplicador_2)
        multiplicador_2 -= 1
        total_2 += soma_2

    segundo_digito = (total_2 * 10 % 11)
    resultado_2 = segundo_digito if segundo_digito <= 9 else 0
    #print(f'O segundo digito de seu CPF deveria ser {resultado_2}.')

    delimiter = ''
    cpf_tratado = delimiter.join(cpf_primeiro_digito)

    try: 
        if int(cpf[9]) != resultado or int(cpf[10]) != resultado_2:
            print('CPF inválido.')
        else:
            print('Validação concluída.')
    except IndexError:
        novo_cpf = (f'O novo CPF é {cpf_tratado}{resultado}{resultado_2}')
        print(novo_cpf)














