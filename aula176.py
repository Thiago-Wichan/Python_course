# Função map para mapear dados
from functools import partial, reduce   


def print_int(iterator):
    print(*list(iterator), sep= '\n')
    print()

produtos = [
     {'nome': 'Produto 5', 'preco': 10.00},
     {'nome': 'Produto 1', 'preco': 22.32},
     {'nome': 'Produto 3', 'preco': 10.11},
     {'nome': 'Produto 2', 'preco': 105.87},
     {'nome': 'Produto 4', 'preco': 69.90},
 ]

# filter

filter_products = filter(lambda p: p['preco'] > 10, produtos)
total = reduce(lambda x, p: x+p['preco'], produtos, 0)

def soma(prev, produto):
    return prev + produto['preco']

total_1 = reduce(soma, produtos, 0)
print(round(total, 1), 'Total')
print(total_1, 'Total 1')

print_int(list(filter_products))

# novos_produtos = [
#     {**p, 'preco': aumentar_valor(p['preco'], 1.1)} for p in produtos
# ]

def aumentar_valor(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_valor_dez_por_cento = partial(aumentar_valor, porcentagem=1.1)


def muda_preco (produto):
    return {
        **produto, 'preco':
         aumentar_valor_dez_por_cento (produto['preco'])
    }

novos_produtos = (list(map(muda_preco, produtos)))



print_int(novos_produtos)



