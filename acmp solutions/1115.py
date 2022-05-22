# acmp.ru
# 1115

n, k = map(int,input().split())
a1 = k // n
a2 = k % n
a3 = n - k % n
print(a1, a2, a2 if k % n == 0 else a3)









