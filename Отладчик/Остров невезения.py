d = int(input())
m = int(input())
if m >= 3 and m <= 12:
    m -= 2
elif m >= 1 and m <= 2:
    m += 10
year = int(input())
y = year % 1000
c = year // 100
z = d + ((13 * m - 1) // 5 ) + y + (y // 4 + c // 4 - 2 * c + 777)
z %= 7
print(z)
