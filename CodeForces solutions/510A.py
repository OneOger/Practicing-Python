# CodeForces
# 510A

n, m = map(int, input().split())
for i in range(1, n + 1):
    for j in range(1):
        if i % 2 != 0:
            print('#' * m)
        elif i % 4 == 0 and i % 2 == 0:
            print('#'.ljust(m, '.'))
        elif i % 2 == 0:
            print('#'.rjust(m, '.'))

