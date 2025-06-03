"""
Dicionário - dict
- Mutável
- Chamado por chave {} ou dict
- Métodos úteis dos dicionários em Python:
    len - quantas chaves
    keys - iterável com chaves
    values - iterável com valores
    items - iterável com chaves e valores
    setdefault - adiociona valor se a chave não existe
    copy - retorna cópia rasa (shallow copy) - cópia rasa, não entra nos subníveis (exemplo: lista ou dicionário)
    get - obtém uma chave
    pop - apaga um item com a chave especifícada (del)
    popitem - apaga o último item adicionado
    update - atuliza um dicionário com outro
    Cópia profunda (deep copy) - import copy e o comando .deepcopy()
"""


pessoa = {
    'Nome': 'Thiago',
    'Sobrenome': 'Wichan',
    'Idade': 30,
    'Peso': '89 Kg',
}

print(pessoa['Nome'])
pessoa.setdefault('Peso', 'Matusalém')
for dados in pessoa:
    print(dados, pessoa[dados])