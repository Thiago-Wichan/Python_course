"""
Argumentos nomeados e nao nomeados nas funções Python
Argumento nomeado tem nome com sinal  de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y):
    print(f'{x = }, {y = }', '|', 'x + y =', (x+y))

soma(1,2)
soma(y=87,x=45) #toda vez que eu nomear um argumento, todos os depois dele deverão ser nomeados também.



