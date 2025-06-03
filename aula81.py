#    LISTAS   #

# Mutável - Suporta valores de qualquer tipo 
# Métodos úteis - append, insert, pop, del, clear, extend
# CRUD - Create, read, Update, Delete
# append - adiciona um elemento ao final da lista
# insert - adiciona um item no índice escolhido
# pop - remove do final ou índice escolhido
# del - apaga um índice
# clear - limpa a lista
# extend - estende a lista
# + - concatena a listas

lista = [10, 20, 30, 40]
lista[2] = 300


del lista[2]

print(lista)

lista.append(50) # Adiciona o valor ao final da lista

print(lista)

lista.pop() 

lista.insert(0, 100)

print(lista)

lista_b = [1,2,3]
lista_c = lista + lista_b
lista.extend(lista_b) # Ação para juntar a lista B em A
lista_b += [2]
print(lista_b)
lista_d = lista.copy() # crio a lista d e incluo os mesmos valores de A, não sendo a mesma lista. Diferente de lista_d = lista
print(lista_c)

