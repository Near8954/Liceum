def average(values):
    if values == []:
        return 0
    else:
        x = sum(values) / len(values)
        if x == int(x):
            return int(x)
        else:
            return x
print(average([-5, 2]))