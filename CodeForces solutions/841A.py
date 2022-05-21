# CodeForces
# 841A

# Option 1 - using dictionary:

baloons, friends = map(int,input().split())
colors = input()
slovar = {}

for i in colors:
    slovar[i] = slovar.get(i, 0) + 1

if max(slovar.values()) > friends:
    print('NO')
else:
    print('YES')


# Option 2 - using counting sort:


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


