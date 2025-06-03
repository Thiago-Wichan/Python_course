produtos = [
     {'nome': 'Produto 5', 'preco': 10.00},
     {'nome': 'Produto 1', 'preco': 22.32},
     {'nome': 'Produto 3', 'preco': 10.11},
     {'nome': 'Produto 2', 'preco': 105.87},
     {'nome': 'Produto 4', 'preco': 69.90},
 ]

import copy
def exibir(x):
    for item in x:
        print(item)
    print()

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in produtos
]
novos_produtos_dc = copy.deepcopy(novos_produtos)
exibir(novos_produtos_dc)
exibir(produtos)

teste_produtos = [
    {**teste, 'nome': teste['nome'].upper()}
    for teste in produtos
]
exibir(teste_produtos)



# Produtos ordenados por preço e deepcopy
produtos_ordenados_por_preco = sorted(produtos, key=lambda item: item['preco'])
produtos_ordenados_por_preco_dc = copy.deepcopy(produtos_ordenados_por_preco)
exibir(produtos_ordenados_por_preco_dc)

# Produtos ordenados por nome e deepcopy
produtos_ordenados_por_nome = sorted(produtos, key = lambda item: item['nome'], reverse=True)
produtos_ordenados_por_nome_dc = copy.deepcopy(produtos_ordenados_por_nome)
exibir(produtos_ordenados_por_nome_dc)






