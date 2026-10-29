def sum_number(nums):
    return sum(nums)


def high_order_function(f, lst):
    summation = f(lst)
    return summation

resultado = high_order_function(sum_number, [1,2,3,4,5,6,7])
print(resultado)