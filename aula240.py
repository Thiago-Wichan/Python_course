# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.

class MyOpen:
    
    def __init__ (self, path_file, mode):
        self.path_file = path_file
        self.mode = mode
        self._file = None

    def __enter__ (self):
        print('Opening File')
        self._file = open(self.path_file, self.mode, encoding='utf8')
        return self._file

    def __exit__ (self, class_exception, exception_, traceback_):
        print('Closing file')
        self._file.close()


with MyOpen('aula240.txt', 'r+') as file:
    file.write('Linha 1 \n')
    file.write('Linha 2 \n')
    print('with', file)


