import random, string

def user_id_gen_by_user():
    quantidade_caracteres = int(input("quantidade de caracteres para sua segurança? "))
    quantidade_id = int(input("quantidade de ids para serem gerados? "))
    lista_ids = []
    caracteres_validos = string.ascii_letters + string.digits
    
    for i in range(quantidade_id):
        id = "".join(random.choices(caracteres_validos, k=quantidade_caracteres))
        lista_ids.append(id)

    for i in range(len(lista_ids)):
        print(lista_ids[i])


user_id_gen_by_user()