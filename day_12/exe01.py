import string 
import random

def random_user_id():
    caracteres_validos = string.ascii_letters + string.digits
    quantidade = 6
    id = "".join(random.choices(caracteres_validos, k=quantidade))

    return id
print(random_user_id())



    
    