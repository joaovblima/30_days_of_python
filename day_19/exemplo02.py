import os 
if os.path.exists('./teste.txt'):
    os.remove('./teste.txt')
else:
    print('arquivo nao existe')