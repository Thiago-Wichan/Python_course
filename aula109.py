"""
Escopo de funções de Python

Escopo significa o local que aquele código pode atingir
Existe o escopo local e global
Global: todo o código é alcançável
Local: apenas nomes do mesmo local podem ser alcançados
Não temos acesso de nomes de escopos internos nos externos
A palavra global faz uma variável de escopo interno ser válida no escopo externo
"""

x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
        x = 11
        y = 2
        print(x, y)
    outra_funcao()
    print(x)
print(x)
escopo()
print(x)

