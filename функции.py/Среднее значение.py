def print_average(arr):
    if arr == []:
        print(0)
    else:
        s = 0
        k = 0
        for i in arr:
            s += i
            k += 1
        print(s / k)
