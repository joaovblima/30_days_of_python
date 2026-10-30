
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
"""


Use filter para filtrar países que comecem com 'E'

"""
new_countries = map(lambda x: x.upper(), countries)
print(list(new_countries))

new_numbers = map(lambda x: x**2, numbers)
print(list(new_numbers))

new_names = map(lambda x: x.upper(), names)
print(list(new_names))

land_countries = filter(lambda x: "land" in x, countries)
print(list(land_countries))

big_countries = filter(lambda x: len(x) == 6, countries)
print(list(big_countries))

big_countries = filter(lambda x: len(x) >= 6, countries)
print(list(big_countries))

e_countries = filter(lambda x: x.startswith("E"), countries)
print(list(e_countries))

