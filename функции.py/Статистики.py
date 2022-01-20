def print_statistics(arr):
    if arr == []:
        for i in range(5):
            print(0)
    else:
        print(len(arr))
        print(sum(arr) / len(arr))
        print(float(min(arr)))
        print(float(max(arr)))
        if len(arr) == 1:
            print(float(arr[0]))
        elif len(arr) % 2 != 0:
            print(sorted(arr)[int(len(arr) / 2)])
        else:
            print((sorted(arr)[len(arr) // 2] + sorted(arr)[len(arr) // 2 - 1]) / 2)
