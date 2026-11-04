import csv

try:
    with open('./csv_exemplo.csv') as f:
        csv_reader = csv.reader(f, delimiter=', ')
        line = 0
        for row in csv_reader:
            if line == 0:
                print(f'column names are:  {", ".join(row)}.')
                line +=1
            else:
                print(f'\t{row[0]} is a teaches. he lives in {row[1]}, {row[2]}')
                line +=1
    
        print(F'lines ->', line)
except FileNotFoundError:
    print('arquivo nao existe')