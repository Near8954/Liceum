n = int(input())
w = 1
summ, c = 0, 0
while summ < n:
    if n > len(str(w)) * w * 10 - 1:
        summ = len(str(w)) * w * 10 - 1
        w *= 10
        c = w 
print(c)
