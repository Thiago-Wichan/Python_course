# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

import calendar

# print(calendar.calendar(1995))
# print(calendar.month(1995, 5))
number_first_day, last_day = calendar.monthrange(1995, 5)
print(calendar.day_name[number_first_day])
print(last_day)
print(calendar.day_name[calendar.weekday(1995, 5, 6)])
