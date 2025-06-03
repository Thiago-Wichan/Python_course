class Multiplicar:
    def __init__(self, multiplicator):
        self._multiplicator = multiplicator

    def __call__(self, func):
        def intern(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * self._multiplicator
        return intern

@Multiplicar(2)
def division(x,y):
    result = x/y
    return result


@Multiplicar(150.85)
def soma (x, y):
    return x + y

two_plus_two = soma (2,2)
print (two_plus_two)
a = division(10, 5)
print(a)