import json

# pessoa = {
#      'nome': 'Luiz Otávio 2',
#      'sobrenome': 'Miranda',
#      'enderecos': [
#          {'rua': 'R1', 'numero': 32},
#          {'rua': 'R2', 'numero': 55},
#      ],
#      'altura': 1.8,
#      'numeros_preferidos': (2, 4, 6, 8, 10),
#      'dev': True,
#      'nada': None,
#  }

# with open('aula190.json', 'w', encoding='utf8') as file:
#     json.dump(
#           pessoa, 
#           file, 
#           indent=2
# ) # caso queira colocar com acentos etc - ensure_ascii = false

# Código acima criou o arquivo aula190.json e abaixo traremos os dados novamente ao arquivo:

with open ('aula190.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)

