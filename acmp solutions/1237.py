# acmp.ru
# 1237

n, m = map(int,input().split())

matr1 = [list(map(int,input().split())) for i in range(n)]
input()
matr2 = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    for j in range(m):
        print(matr1[i][j] + matr2[i][j], end=' ')
    print()



