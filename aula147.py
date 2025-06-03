# Introdução à Generator function


# def generator (n=0):
#     yield 1 # Pausa a função
#     print('Continuando...')


# gen = generator(n=0)
# print(next(gen))
# print(next(gen))

def generator (n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return
gen = generator(n=0, maximum=1000)       
for n in gen:
    print(n)



