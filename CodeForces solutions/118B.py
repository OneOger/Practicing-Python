# CodeForces
# 118B

n = int(input())
space = n * 2

for i in range(n + 1):  # first part from 0 to n;
    s = []
    for j in range(i):
        s.append(j)
    print(space * ' ', end='')  # Doing this because of extra space from 'sep';
    print(*s, i, *s[::-1])
    space -= 2

space = 2
for i in range(n - 1, -1, -1):  # second part from n-1 to 0;
    s = []
    for j in range(i):
        s.append(j)
    print(space * ' ', end='')
    print(*s, i, *s[::-1])
    space += 2



