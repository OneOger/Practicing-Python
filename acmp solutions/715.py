# acmp.ru
# 715


n, m = map(int,input().split())

a = [input() for i in range(n)]
input()
b = [input() for i in range(n)]
count = 0

print(a)
for i in range(n):
    for j in range(m):
        if a[i][j] == b[i][j]:
            count += 1

print(count)







