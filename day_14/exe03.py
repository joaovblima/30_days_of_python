from functools import reduce


num = [i for i in range(21)]


result = reduce(lambda x, y: x + y, map(
    lambda x: x, filter(lambda x: x % 2 ==0, num)
))

print(result)