# Mapeamento de dados em list comprehension
import pprint

def p(x):
    pprint.pprint(x, sort_dicts=False, width=40)


produtos = [
    {'Nome': 'p1', 'Preço': 20,},
    {'Nome': 'p2', 'Preço': 10,},
    {'Nome': 'p3', 'Preço': 30,},
]

# print(produtos)

# novos_produtos = [
#     {**produto, 'Preço': produto['Preço'] * 1.1}
#     if produto['Preço'] > 20 else {**produto}
#     for produto in produtos
# ]


# print(*novos_produtos, sep='\n')
# p(novos_produtos)
    
novos_produtos = [
    {**produto, 'Preço': produto['Preço'] * 1.1}        
    if produto['Preço'] >= 20 else {**produto}      #Antes do for é mapeamento
    for produto in produtos
    if produto['Preço'] > 10                        #Depois do for é filtro
]



p(novos_produtos)
