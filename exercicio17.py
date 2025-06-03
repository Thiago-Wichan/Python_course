# Lista com refazer e desfazer
import os
import json

list = []
list_2 = []

def impression (list):
    print()
    print('Tarefas:')
    for items in list:
        item_capitalize = items.capitalize()
        print (f'\t {item_capitalize}', sep='\n')
    print()

with open ('lista_exercicio_17.json', 'r', encoding='utf8') as arquivo:
    list = json.load(arquivo)
    impression(list)
with open ('lista_exercicio_17.json', 'r', encoding='utf8') as arquivo:
    list_2 = json.load(arquivo)

# Function to execute others functions
def execution (func, list=list):
    if list:
        func()
        return
    if not list:
        print()
        print('A lista está vazia.')
        print()   
    execution

# Function to exclude a item from list           
def exclusion (list=list):
    list.pop()

# Function to bring back items on list
def undo (list=list, list_2=list_2):
    x = len(list) - len(list_2)
    if x == 0:
        print()
        return print('Não há itens a serem refeitos. \r\n')
    list.append(list_2[x])


while True:

    data = input(
        'O que você deseja fazer?\r\n'
        'Listar / Desfazer / Refazer: '
    ).lower()
    

    if data == 'listar':
        execution(impression(list), list)
        continue

    if data == 'desfazer':
        execution(exclusion)
        impression(list)
        continue

    if data == 'refazer':
        undo()
        impression(list)
        continue
    
    # Clean console
    if data == 'clear':
        os.system('cls')
        continue

    if data == 'salvar':
        with open ('lista_exercicio_17.json', 'w', encoding='utf8') as arquivo:
            json.dump(
            list,
            arquivo,
            indent=2
)              
            os.system('cls')
            impression(list)
            print('Sua lista foi salva.')
            print()
        continue

    list.append(data)
    list_2.append(data)
    


    

    

