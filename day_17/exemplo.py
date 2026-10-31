try:
    name = input("enter yout name: ")
    year_born = input("year you are born? ")
    age = 2019 - year_born
    print(f'you are {name}, and your age is {age}')
except Exception as e:
    print(e)