"""
split e join com list e str
split - divide uma string
join - une uma string
strip - cortar espaços a direita e esquerda - lstrip (esquerda) e rstrip (direita)
"""

frase = 'Olha, que coisa interessante.'
lista_palavras = frase.split() # possibilidade de usar o argumento para escolher o carácter
                               # que dividirá
print(lista_palavras)

lista_virgula = frase.split(',')
print(lista_virgula)



