def find_mountain(heightsMap):
    a = []
    for i in heightsMap:
        a.append(max(i))
    x = max(a)
    for i in range(len(heightsMap)):
        if x in heightsMap[i]:
            s = i
            break
    for i in range(len(heightsMap[s])):
        if heightsMap[s][i] == x:
            stolb = i
            break
    return s, stolb
print(find_mountain([[2, 4, 2, 3, 2], [3, 2, 3, 4, 3]]))

