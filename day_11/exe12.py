def evens_and_odds(num):
    count_evens = 0
    count_odds = 0

    for i in range(num+1):
        if i % 2 ==0:
            count_evens +=1
        else:
            count_odds +=1

    text = f"The numers of odds is {count_odds} and the numbers of evens is {count_evens}"

    return text

print(evens_and_odds(100))