# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
date_1 = datetime.strptime('06/05/1995 15:00:00', fmt)
date_2 = datetime.now()
# delta = date_2 - date_1

delta = relativedelta(date_2, date_1)

print(f'{delta.years} Anos, {delta.days} Dias, {delta.hours} Horas,'
      f' {delta.minutes} Minutos e {delta.seconds} Segundos.')

# print(delta.days)
# print(date_2)
# print(date_2 + relativedelta(minutes=37))
