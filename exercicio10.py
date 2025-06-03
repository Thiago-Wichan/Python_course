
def multiplicador(x):
    def argumento(y):
        return x*y
    return argumento

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

entrada = input('Digite um número a ser multiplicado por 2: ')
print(duplicar(int(entrada)))