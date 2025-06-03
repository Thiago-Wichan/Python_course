# Enumerar listas - enumerate

lista = ['Maria', 'João', 'Pedro']
lista.append('José')
lista_enumerada = enumerate(lista)

for indice, nome in enumerate(lista):
    print(indice, nome)
