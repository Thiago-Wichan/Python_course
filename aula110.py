# Retorno do valor das funções (return)
# args são argumentos não nomeados para a função
# *args - empacotamento e desempacotamento


def soma (x, y):
    return x + y #caso usasse a função print, o valor retornado pela função seria None

soma1 = soma(2, 2)
soma2 = soma(3, 3)

# print(soma1 + soma2)


def somas (*args):      
    total = 0  
    for numero in args:
        total += numero
    return total


print(somas (1, 2, 10, 20))
num_lists = [[1, 2, 3], [4, 6, 8]]

combined_list = sum(num_lists, [])

print(combined_list)

chama = (1, 2, 3, 4, 5)
print(sum(chama, 10))