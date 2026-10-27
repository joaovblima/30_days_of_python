frutas = ['banana', 'orange', 'mango', 'lemon']
new_frutas = []
for i in range(len(frutas)):
    fruta = frutas.pop()
    new_frutas.append(fruta)
print(new_frutas)