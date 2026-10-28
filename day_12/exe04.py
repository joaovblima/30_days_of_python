import random, string
def list_of_hexa():
    list = []
    id="#"
    caracteres = string.ascii_letters + string.digits
    quantidade = 6
    id2 = "".join(random.choices(caracteres, k=quantidade))
    id +=id2
    list.append(id)
    return list

print(list_of_hexa())