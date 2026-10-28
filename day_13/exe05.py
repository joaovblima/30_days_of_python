produtos = [
    {"nome": "Notebook", "preco": 3000},
    {"nome": "Mouse", "preco": 100},
    {"nome": "Monitor", "preco": 900},
    {"nome": "Teclado", "preco": 200}
]

lista_produtos = [
    produto["preco"] 
    for produto in produtos
    if produto["preco"] > 500
]

print(lista_produtos)