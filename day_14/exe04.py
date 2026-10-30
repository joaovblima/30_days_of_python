
def get_string_lists(lista):
    n_l = filter(lambda x: type(x) == str, lista)
    return list(n_l)


lista = ['jaao', 3, 4, 5, "vamo", 'vai brasil']

print(get_string_lists(lista))