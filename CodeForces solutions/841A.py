# CodeForces
# 841A

n, k = map(int, input().split())
balloons = input()
count = [0] * 26
z = 0

for i in balloons:
    number = ord(i) - 97
    count[number] += 1

for i in range(26):
    if count[i] > 0:
        if count[i] <= k:
            z += 1
        else:
            z -= 1000

if z > 0:
    print('YES')
else:
    print('NO')


