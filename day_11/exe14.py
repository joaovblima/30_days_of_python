def greet(nome=None):
    if nome is None:
        print("Hello, Guest!")
    else:
        print("Hello", nome.capitalize())

greet()
greet("joao")