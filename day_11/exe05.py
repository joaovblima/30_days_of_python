def check_season(mes):
    inverno = ['dezembro', 'janeiro', 'fevereiro']
    outono = ['setembro', 'outubro', 'novembro']
    primavera = ['março', 'abril', 'maio']
    verao = ['junho', 'julho', 'agosto']

    
    if mes.lower() in inverno:
        return 'Inverno'
    elif mes in outono:
        return 'Outono'
    elif mes in primavera:
        return 'Primavera'
    else:
        return 'Verão'

print(check_season("janeiro"))