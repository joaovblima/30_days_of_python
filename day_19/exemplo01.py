arquivo = './teste.txt'
try:
    file = open(arquivo, 'r')
except FileNotFoundError:
    print('file not founder papai')
    
