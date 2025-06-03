# kwargs - keyword arguments (argumentos nomeados)

def mostra_pessoa_completa(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)


mostra_pessoa_completa(Nome='Joana')

