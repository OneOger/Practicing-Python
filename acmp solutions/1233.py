# acmp.ru
# 1233

a = []
n = int(input())

for i in range(n):
    a.append(list(map(int, input().split())))

b = [i[::] for i in a]

for i in range(n):
    for j in range(n):
        if i < j:
            b[i][j] = b[j][i]

for i in range(n):
    for j in range(n):
        if i > j:
            b[i][j] = a[j][i]

print()
for i in b:
    print(*i)




