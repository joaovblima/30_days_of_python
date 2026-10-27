my_age = 29
your_age = int(input("your age? "))

diferenca = your_age - my_age
diferenca_minha = my_age - your_age
if your_age > my_age:
    if diferenca > 1:
        print('You are', diferenca, 'years older than me')
    else:
        print('You are 1 year older than me')
else:
    print('I am', diferenca_minha, 'years old than you')