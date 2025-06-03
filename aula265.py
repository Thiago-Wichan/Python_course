# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
# asdict e astuple convertem a classe para um dicionário

from dataclasses import astuple, dataclass, asdict


@dataclass
class Person:
    name: str
    age: int


p1 = Person('Thiago', 30)
print(p1)
p2 = Person('Jucelino', 20)
print(p1 == p2)
p3 = Person('Thiago', 30)
print(p3 == p1)
print(astuple(p1))
print(asdict(p2))
