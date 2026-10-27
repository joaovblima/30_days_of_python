def sum_of_odds(num):
    sum_odd = 0
    for i in range(num+1):
        if i % 2 != 0:
            sum_odd += i

    return sum_odd

def sum_of_even(num):
    sum_even = 0
    for i in range(num+1):
        if i % 2 ==0:
            sum_even += i
    return sum_even
    
print(sum_of_odds(10))
print(sum_of_even(10))
