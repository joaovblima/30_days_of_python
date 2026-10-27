inverno = ['dezembro', 'janeiro', 'fevereiro']
outono = ['setembro', 'outubro', 'novembro']
primavera = ['março', 'abril', 'maio']
verao = ['junho', 'julho', 'agosto']

mes = input('Digite o mês: ')
mes = mes.lower()
if mes in inverno:
    print('Inverno')
elif mes in outono:
    print('Outono')
elif mes in primavera:
    print('Primavera')
else:
    print('Verão')