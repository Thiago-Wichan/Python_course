palavra_secreta = "frango"
letra_acertada = ''
numero_tentativas = 0
import os


while True:
    tentativa = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(tentativa) > 1:
        print('Digite apenas uma letra.')
        continue
    if tentativa in palavra_secreta:
        letra_acertada += tentativa
   
    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
        
    print(f'A palavra formada é: "{palavra_formada}"')       
    
    if '*' not in palavra_formada:
        os.system('cls')
        print(f'Parabéns, você conseguiu! A palavra secreta é "{palavra_secreta}"')
        print('Você tentou', numero_tentativas,'x até conseguir.')

        break



    
