# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
from pytz import timezone

# date_str = '2025-05-22 10:33:00'
# date_str_fmt = '%Y-%m-%d %H:%M:%S'
# date = datetime(2025, 5, 22, 10, 33)
# date = datetime.strptime(date_str, date_str_fmt)
date = datetime.now(timezone('Asia/Tokyo'))

print(date)
