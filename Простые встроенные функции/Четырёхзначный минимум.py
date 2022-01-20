num = int(input())
a = num // 1000
b = num // 100 % 10
c = num // 10 % 10
d = num % 10
if a > b and a and b:
    a, b = b, a
if b > c:
    b, c = c, b
if c > d:
    d, c = c, d
if a > b and a and b:
    a, b = b, a
if b > c:
    b, c = c, b
if c > d:
    d, c = c, d
if a > b and a and b:
    a, b = b, a
if b > c:
    b, c = c, b
if c > d:
    d, c = c, d
if a > c and c:
    a, c = c, a
if a > d and d:
    a, d = d, a
print(str(a) + str(b) + str(c) + str(d))