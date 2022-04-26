# acmp.ru
# 1236

a = []
n, m = map(int,input().split())

for i in range(n):
    a.append(list(map(int,input().split())))

for i in range(len(a)-1,-1,-1):
    print(*a[i])


