def packing_person_info(**kwargs):
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')

    return kwargs


print(packing_person_info(nome="joao", pais='brasil', cidade='uniao dos palmares', idade=30))
