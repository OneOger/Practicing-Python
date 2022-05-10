# CodeForces
# 707A


n, m = map(int, input().split())
b = [list(input().split()) for i in range(n)]
count = 0

for i in range(n):
    for j in range(m):
        if b[i][j] != 'W' and b[i][j] != 'G' and b[i][j] != 'B':
            count += 1

if count == 0:
    print('#Black&White')
else:
    print('#Color')






