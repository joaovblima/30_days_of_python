countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_countries = [
    {"country": cidade[0], 
        "city": cidade[1]}
    for pais in countries for cidade in pais
]

print(dict_countries)