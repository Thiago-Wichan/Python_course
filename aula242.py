from contextlib import contextmanager

@contextmanager
def open_file (file_path, mode):
    try:
        print ('Opening file')
        file = open(file_path, mode, encoding='utf8')
        yield file

    except Exception as e:
        print ('An ERROR occurred', e)
    
    finally:
        print ('Closing file')
        file.close()

with open_file('aula242.txt', 'r') as file:
    file.write ('Linha 1 \n')
    file.write('Linha 2 \n')
    print ('with', file)

