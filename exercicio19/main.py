from log import LogFileMixin, LogPrintMixin
from eletronic import Smartphone

iphone = Smartphone('iPhone')
samsung_s24 = Smartphone('Samsung S24')


iphone.turn_on()
samsung_s24.turn_off()


# ls = LogFileMixin()
# ls.log_error('qualquer coisa')
# ls.log_sucess('Deu certo')


# lp = LogPrintMixin()
# lp.log_error('qualquer coisa')
# lp.log_sucess('Deu certo')
