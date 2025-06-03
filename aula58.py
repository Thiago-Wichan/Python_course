# docs.python.org - Biblioteca python

# Repetições
# While - executa uma função enquanto ela for verdadeira


condicao = True

while condicao: # while será executado enquanto a condição for vdd, se falsear, deixa de ser executada.
    nome = input('Qual o seu nome?: ')
    print(f'Seu nome é {nome}')
    if nome == 'sair':
        break

print('Voce saiu do looping eterno')