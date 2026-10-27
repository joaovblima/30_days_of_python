"""
idade = 29
altura = 1.80
equacao = 4 + 4j
base = int(input("qual a base? "))
altura_triangulo = int(input("qual a altura do triangulo? "))
area_tri = base * altura_triangulo
print("a área do triângulo é ", area_tri)

a = int(input("Enter side a: "))
b = int(input("Enter side b"))
c = int(input("Enter side c: "))
perimetro = a + b + c
print("The perimeter of the triangle is", perimetro)

comprimento = float(input("Comprimento: "))
largura = float(input("Largura: "))
area_dois = comprimento * largura
perimetro_dois = 2 * (comprimento + largura)
print("area dois", area_dois)
print("perimetro dois", perimetro_dois)

raio_circulo = float(input("raio do circulo: "))
area_do_circulo = 3.14 * raio_circulo * raio_circulo
circunferencia_circulo = 2 * 3.14 * raio_circulo
print("area do circulo: ", area_do_circulo)
print("circunferencia do circulo: ", circunferencia_circulo)

tam_python = len("python")
tam_dragon = len("dragon")

print("tam python é maior que tam dragon? ", tam_python > tam_dragon)
on_in_python_dragon = "on" in "dragon" and "python" 
print(on_in_python_dragon)
frase_jargao = "I hope this course is not full of jargon"
print("jargon" in frase_jargao)
len_de_python = len("python")
float_len_de_python = float(len_de_python)
print(str(float_len_de_python))
print(10 % 2 == 0)
print(type('10' == type(10)))
print(7/3 == int(2.7))
print(int(9.8) == 10)

hours = int(input("enter hours: "))
price_hours = int(input("enter rate per hours: "))
total_order = hours * price_hours 
print("your weakly earn is", total_order)


years_lived = int(input("Enter number of years you have lived: "))
seconds_per_day = 24 * 60 * 60
seconds_per_year = 365 * seconds_per_day
year_lived_in_seconds = seconds_per_year * years_lived
print("You have lived for", year_lived_in_seconds, "seconds.")
"""
script = """1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125 """
print(script)