nome = input('Digite seu nome aqui: ')
idade = input('Digite sua idade aqui: ')

if nome != '' and idade != '':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome contém {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[:1]}')
    print(f'A última letra do seu nome é {nome[-1:]}')
    if ' ' in nome:
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço')    
else:
    print('Desculpe, você deixou campos vazios')

