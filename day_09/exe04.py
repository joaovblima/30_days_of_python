"""
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
"""
nota = int(input("Qual sua nota? "))

if nota <= 59:
    print('F')
elif nota <=69:
    print('D')
elif nota <=79:
    print('C')
elif nota <=89:
    print('B')
else:
    print('A')