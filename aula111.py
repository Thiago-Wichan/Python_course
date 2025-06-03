# High order function

# Higher Order Functions - Funções que podem receber e/ou retornar outras funções

# First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

# Closure e funções que retornam outras funções

# def m1(x):        
#     return x*2

# def m2(x):
#     return x*3

# def m3(x):
#     return x*4

# x = 10
# print(m1(x))
# print(m2(x))
# print(m3(x))

def multiplicador(multi):
    def multiplicar(numero):
        return numero * multi
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

print(duplicar(100))
print(triplicar(15))
print(quadruplicar(50))

for numero in range (1,11):
    # print(duplicar(numero))
    print(triplicar(numero))



