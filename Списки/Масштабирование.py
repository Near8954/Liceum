n = int(input())
m = int(input())
pic = []
for i in range(n):
    pic.append(input())
pic = pic[::2]
for i in range(len(pic)):
    pic[i] = pic[i][::2]
for i in pic:
    print(i)
