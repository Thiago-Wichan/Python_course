def multi(*arg):
    multiplicador = 1
    for num in arg:
        multiplicador *= num    
    return multiplicador

print(multi(2, 10, 73, 87))


def par(x):
    if x % 2 == 0:  
        return (f'O número {x} é par.')
    return (f'O número {x} é ímpar.')


print(par(5165165))



