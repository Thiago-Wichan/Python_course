hora = input('Que horas são? ')
manha = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')
tarde = ('12', '13', '14', '15', '16', '17')
noite = ('18', '19', '20', '21', '22', '23')


if hora in manha:
    print('Bom dia')
elif hora in tarde:
    print('Boa tarde')
elif hora in noite:
    print('Boa noite')