# Variáveis livres e nonlocal

def fora(x):
    variavel_fora = x
    def dentro(y):
        print(locals())
        nonlocal variavel_fora #utilização de nonlocal para usar uma variável de outro escopo nesse
        variavel_fora = x+y
        return variavel_fora
    return dentro

f = fora('a')

print(f('b'))

