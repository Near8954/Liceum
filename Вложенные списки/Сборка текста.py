por = input().split()
s = input().lower().split()
for i in range(len(por)):
    por[i] = int(por[i])
    por[i] -= 1
end = ''
for i in por:
    end += str(s[i]) + ' '
print(end.capitalize()[:-1])