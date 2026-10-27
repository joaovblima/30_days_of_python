fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('Enter yout fruit? ')
fruit = fruit.lower()
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruit, 'alread add in list of fruits')
    print(fruits)