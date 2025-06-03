# As importações devem sempre ser consideradas em relação ao main, mesmo que isso faça com que a
## importação não funcione naquele módulo e apenas no main, exemplo da importação pelo caminho da pasta
### aula 158
# Utiliação do __init__ para transformar o comportamento de um package em um módulo, importando todos
# os dados dos módulos atrelados ao package pelo init. (aula 159)

from sys import path

from aula157_package.moduloaula157 import soma_simples

print(soma_simples(10, 2))

# print(*path, sep='\n')

