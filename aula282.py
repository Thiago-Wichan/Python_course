# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.

import os.path

# path = os.path.join('C:', '\\Users', 'thiag',
#                     'Documents', 'Python')
# print(path)
# print(os.path.exists(path))
# print(os.path.exists(path_2))

# print(os.path.split(path))
# path_2, file_2 = os.path.split(path)

# print(file_2)

path = os.path.join('C:', '\\Users', 'thiag',
                    'Documents', 'Python')

for folder in os.listdir(path):
    complete_path = os.path.join(path, folder)
    print(complete_path)

    # if not os.path.isdir(complete_path):
    #     continue
    # for file in os.listdir(complete_path):
    #     print(file)
