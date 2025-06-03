"""
Introdução às funções (def) em Python
- Trechos de códigos usados para replicar determinada ação ao longo do código
- Podem receber valores p/ parâmetros (argumentos) e retornar um valor específico
Por padrão, funções no Python retornam None
- Parâmetro é o nome da "variável" dentro dos parênteses, argumento é o valor passado para o parâmetro no momento da execução da função.
"""


def imprimir():
    print('varias1')
    print('varias2')

imprimir()

def saudacao(nome = 'Sem nome'):        

    print(f'Olá, {nome}, tudo bem?')


saudacao('Mariazinha')
saudacao('Chumbin')
saudacao() #Caso seja definido o parametro da função, quando em branco ele será executado, conforme essa linha de exemplo



