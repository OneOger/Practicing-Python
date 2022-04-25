# acmp.ru
# 1234

a = []
n = int(input())

for i in range(n):
        a.append(list(map(int,input().split())))

for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        print(a[j][i],end=' ')
    print()




