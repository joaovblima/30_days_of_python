def add_all_nums(*nums):
    sum = 0
    for i in nums:
        if type(i) == int:
            sum += i

    return sum

print(add_all_nums(2, 3, 4, 5, True, "joao"))