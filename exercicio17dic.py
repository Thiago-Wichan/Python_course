# Lista com refazer e desfazer
import os
import json

list = []
list_2 = []

# Function to impress
def impression (list=list):
    print()
    print('Tarefas:')
    for items in list:
        item_capitalize = items.capitalize()
        print (f'\t {item_capitalize}', sep='\n')
    print()

# Function to execute others functions
def execution (func, list=list):
    if list:
        func()
    else:
        print()
        print('A lista está vazia.')
        print()

# Function to exclude a item from list           
def exclusion (list=list):
    list.pop()
    impression()

# Function to bring back items on list
def undo (list=list, list_2=list_2):
    x = len(list) - len(list_2)
    if x == 0:
        print()
        return print('Não há itens a serem refeitos. \r\n')
    list.append(list_2[x])
    impression()

def add (list, list_2, data):
    list.append(data)
    list_2.append(data)
    impression()

while True:

    data = input(
        'O que você deseja fazer?\r\n'
        'Listar / Desfazer / Refazer: '
    ).lower()
    
    comando = {
        'listar': lambda: execution(impression),
        'desfazer': lambda: execution(exclusion),
        'refazer': lambda: execution(undo),
        'clear':  os.system('cls'),
        'adicionar': lambda: add(list=list, list_2=list_2, data=data), 
    }
    
    if comando.get(data) is not None:
        comando.get(data)
    else:
        comando['adicionar']
        with open ('lista_exercicio_17.json', 'w', encoding='utf8') as arquivo:
            json.dump(list, arquivo)
    




