numero = input('Digite um número inteiro: ')



if numero.isdigit(): # A função .isdigit verifica se todos os carcteres de uma str são números.
    conta_numero = (int(numero))
    verificacao_par = ( conta_numero % 2 == 0) 
    if verificacao_par:
        print('Seu número é par')
    else:
        print('Seu número é impar')    
else:
    print('Digite um número inteiro')        




