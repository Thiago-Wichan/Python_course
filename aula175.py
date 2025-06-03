# groupby - grouping values (itertools)
from itertools import groupby

alunos = [
     {'nome': 'Luiz', 'nota': 'A'},
     {'nome': 'Letícia', 'nota': 'B'},
     {'nome': 'Fabrício', 'nota': 'A'},
     {'nome': 'Rosemary', 'nota': 'C'},
     {'nome': 'Joana', 'nota': 'D'},
     {'nome': 'João', 'nota': 'A'},
     {'nome': 'Eduardo', 'nota': 'B'},
     {'nome': 'André', 'nota': 'A'},
     {'nome': 'Anderson', 'nota': 'C'},
 ]

def ordena(x):
    return x['nota']



alunos_agrupados = sorted(alunos, key= ordena)
alunos_nota = groupby(alunos_agrupados, key= ordena)

for chave, grupo in alunos_nota:
    print(chave)
    for aluno in grupo:
        print(aluno)


