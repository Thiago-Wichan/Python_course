"""
Lista de lista e seus índices
"""

sala = [
    ['Maria', 'Helena'], ['Elaine'], ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)]
]

comodoro = ['avião', 'pássaro', 'epírito']

print(sala[0][1])
print(sala[2][3][2])

print(*comodoro, end='.\n', sep='/')

print(*sala, sep='\n', end='\t')






