def factorial(num):
    fat = 1
    for i in range(1, num+1, 1):
        fat *= i

    return fat

print(factorial(5))
        