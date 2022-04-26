# acmp.ru
# 1235

a = []
n, m = map(int,input().split())

for i in range(n):
    a.append(list(map(int, input().split())))


for i in a:
    print(*i[::-1])




