list1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list2 = ['BA', 'SP', 'MG', 'RJ']
new_list = []
l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

# Objetivo é unir as duas listas, pela menor lista

def generator(func):
    def argument(*args, **kwargs):
        new_argum = func(*args, **kwargs)
        return new_argum
    return argument

@generator
def concatenation(x, y):
    global list1, list2
    return [(f'{list1[x]}, ' + f'{list2[y]}')]
    

def concatenation_l(x, y):
    global l1, l2
    return [l1[x] + l2[y]]


index_l = min(len(l1), len(l2))
index_list = min(len(list1), len(list2))


for i in range(index_list):
    new_list += concatenation(i, i)

new_list_l = []  
for i in range(index_l):
    new_list_l += concatenation_l(i, i)
   
print(new_list)  
print(list(zip(list1, list2))) 
# print(new_list_l)

def zipper(l1, l2):
    interval = min(len(l1), len(l2))
    return [
        (l1[i] + l2[i])
        for i in range(interval)
    ]

print(zipper(l1, l2))
from itertools import zip_longest

#Usando o zip e soma, ficaria:

lista_soma = [x + y for x, y in zip((l1), (l2))]
lista_soma2 = [x + y for x, y in zip_longest((l1), (l2), fillvalue=0)]

print(list(lista_soma))
print(list(lista_soma2))







