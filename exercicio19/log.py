# Abstração
from pathlib import Path

project_path = Path()
print(project_path.absolute())

file_path = Path(__file__).parent / 'log.txt'

class Log:
    def _log (self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error (self, msg):
        return self._log(f'Error: {msg}')

    def log_sucess (self, msg):
        return self._log(f'Sucess: {msg}')

class LogFileMixin (Log):
    def _log (self, msg):
        msg_formatted = f'{msg}'
        with open (file_path, 'a', encoding='utf8') as file:
            file.write(msg_formatted)
            file.write('\r\n')


class LogPrintMixin (Log):
    def _log (self, msg):
        print(msg)


if __name__ == '__main__':
    lp = LogFileMixin()
    lp.log_error('qualquer coisa')
    lp.log_sucess('Deu certo')
    