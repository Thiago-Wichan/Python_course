lista = []
indices = []
import os


while True:
    for indice, item in enumerate(lista):
        indices.append(indice)
    
    adicao = input(f'Selecione uma opção:\n[i]ncluir, [a]pagar, [l]istar: ')
    
    

    if adicao == 'i':
        incluir = input('Inclua um item: ')
        lista.append(incluir)
        os.system('cls')
        continue
        
    if adicao == 'l':
        for indice, item in enumerate(lista):
            print(indice, item)
            continue       
    
    if adicao == 'a':        
        remover = int(input('Digite o índice do item que deseja excluir: '))
        if remover in indices:
            lista.pop(remover)
            os.system('cls')
            continue
        else:
            print('Impossível excluir esse índice.')   
        