from datetime import date, datetime
hoje = date(year = 2026, month = 10, day = 30)
ano_nome = date(year = 2027, month= 1, day= 1)
diferenca = ano_nome - hoje

print(diferenca)