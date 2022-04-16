a = list(input())
b = list(input())
c = []

for i in range(len(a)):
    if a[i] != b[i]:
        c.append(1)
    else:
        c.append(0)

print(*c,sep='')