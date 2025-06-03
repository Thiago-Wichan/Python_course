"""
Combinations, permutations and product - itertools
Combinations - order does not matter - iterable
permutations - order matters
product - order matters and repeats unique values
"""
from itertools import combinations, permutations, product

pessoas = [
    'João', 'Maria', 'Thiago', 'Raquel'
]

camisetas = [
    ['preta', 'branca'],
    ['algodão', 'dry fit'],
    ['p', 'm', 'g'],
]

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))

