# acmp.ru
# 1232

n, m = map(int,input().split())
a = []

for i in range(n):
    b = []
    for j in range(1):
        a.append(list(map(int,input().split())))

for i in range(n):
    s = 0
    for j in range(m):
        s += a[i][j]
    print(s,end=' ')
print()

for i in range(m):
    s = 0
    for j in range(n):
        s += a[j][i]
    print(s, end=' ')
print('\n')

for i in a:
    print(*i)



