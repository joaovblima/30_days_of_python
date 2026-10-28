new_list = [(i, ) + tuple(i ** exp for exp in range(6)) for i in range(11)]
print(new_list)