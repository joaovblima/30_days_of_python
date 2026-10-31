def unpacking_person_info(name, country, city, age):
    try:
        return f'{name} lives in {country}, {city}. He is {age} year old'
    except Exception as e:
        return e

dct = {'name': 'joao', 'country': 'brasil', 'city': 'uniao dos palmares', 'age':29}

#se passar o dicionario sozinho, sem mostrar que é um desempacotamento, vai causar um erro, um Type Error, vamos ajeitar na funcao
print(unpacking_person_info(**dct))

