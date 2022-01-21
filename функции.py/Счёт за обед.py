

def count_food(days):
    summ = 0
    for i in days:
        summ += daily_food[i - 1]
    return summ


daily_food = [0, 150, 150]
print(count_food([2, 3]))