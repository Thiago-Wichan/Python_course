nome = input('Digite seu nome: ')
contagem = len(nome)


if contagem <= 4 and contagem > 1:
    print('Seu nome é muito curto')
elif contagem >= 5 and contagem <= 6:
    print ('Seu nome é normal')
elif contagem >= 6:
    print('Seu nome é muito grande')
else:
    print('Digite nome com mais de uma letra')
