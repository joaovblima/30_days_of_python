from functools import reduce


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
acc = "are north European countries"
frase = reduce(lambda x, y: f"{x}, {y}", countries[:-1])
f_frase = f"{frase}, e {countries[-1]} {acc}"
print(f_frase)