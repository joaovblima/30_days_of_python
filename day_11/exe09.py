def remove_item(list, item):
    if item in list:
        list.remove(item)
    return list

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))