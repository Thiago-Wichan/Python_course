# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

loan_value = 1_000_000
loan_term = range(1, 61)
loan_date = datetime(2020, 12, 20)
delta = relativedelta(months=1)

# print(loan_date + delta)
installment_value = (loan_value / 60)

for i in loan_term:
    delta = relativedelta(months=i)
    result = loan_date + delta
    print(f'{datetime.strftime(result, '%d/%m/%Y')}'
          f'- R$ {installment_value:,.2f}')
