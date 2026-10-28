import random, string
def generate_colors(tipo, quantidade):
    lista = []
    caracteres = string.ascii_letters + string.digits
    
    if tipo == "hexa":
        for i in range(quantidade):
            id = "#"+"".join(random.choices(caracteres, k=6))
            lista.append(id)

    elif tipo == "rgb":
        for i in range(quantidade):
            
    return lista


print(generate_colors("hexa", 3))
            
            