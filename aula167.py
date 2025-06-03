


def decoradora(func):
    print('Decoradora 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        resolution = func(*args, **kwargs)
        return resolution
    return aninhada

@decoradora
def soma(x, y):
    return x+y


ten_plus_five = soma(5, 10)

print(ten_plus_five)
