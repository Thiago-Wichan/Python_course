# Intodução ao desempacotamento + tuples (tuplas)

nome1, *_ = ['Maria', 'Joao', 'Pedro'] # o asterisco permite criar uma variável residual

print(nome1)

print(*_)

# tuple = é uma lista imutável. formas de se fazer uma tuple:
# 
# - Não usar os colchetes
# - Utilizar parenteses ()
# - criar uma variável nova = tuple(lista)

lista = ['Maria', 'João', 'Pedro']
lista_imt = tuple(lista) #inverso também é válido

print(lista_imt)

