list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista = [i for linha in list_of_lists for i in linha ]
print(lista)

#[1, 2, 3, 4, 5, 6, 7, 8, 9]