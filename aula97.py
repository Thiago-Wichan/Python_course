"""
Operação Ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""
condicao = 1==10
variavel = 'Valor' if condicao else 'Outro valor'

print(variavel)

digito = 20
novo_digito = digito if digito <= 9 else 0

print(novo_digito)


