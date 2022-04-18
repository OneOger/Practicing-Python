# CodeForces
# 405A

# Option 1 - using counting sort:

n = int(input())
cubes = list(map(int,input().split()))
m = max(cubes)+1
count = [0]*m

for i in cubes:
    count[i] += 1

for i in range(m):
    if count[i] > 0:
        print((str(i) + ' ') * count[i], end='')

# Option 2 - using sort() function.

n = int(input())
cubes = list(map(int,input().split()))
cubes.sort()
print(*cubes)


