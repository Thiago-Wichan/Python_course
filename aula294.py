import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / 'aula294.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

# with open(CSV_PATH, 'w') as file:
#     collumns_name = lista_clientes[0].keys()
#     writer_ = csv.DictWriter(file, fieldnames=collumns_name)

#     writer_.writeheader()

#     for i in lista_clientes:
#         writer_.writerow(i)

lista_clientes_list = [
    ['Luiz Otávio', 'Av 1, 22'],
    ['João Silva', 'R. 2, "1"'],
    ['Maria Sol', 'Av B, 3A'],
]

with open(CSV_PATH, 'w') as file:
    collumns_name = ['Name', 'Adress']
    writer_ = csv.writer(file)

    writer_.writerow(collumns_name)

    for i in lista_clientes_list:
        writer_.writerow(i)
