# isistance - para saber se o objeto é determinado tipo

lista = [
    'a', 1, 1.1, True, [0,1,2,3], {0,1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print(item)

    elif isinstance(item, dict):
        print (item)

    elif isinstance(item, list):
        print('List')
        print(item)

    elif isinstance(item, (int, float)):
        print('Numeral')
        print(item / 0.5)
        

    