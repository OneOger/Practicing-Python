# CodeForces
# 1015A

n, m = map(int,input().split())
points = [] # or points = [i for i in range(1, m + 1)]:

for i in range(1, m + 1):
    points.append(i)

for i in range(n):
    start, end = map(int,input().split())
    for i in range(start, end + 1):
        if i in points:
            points.remove(i)

print(len(points))
for i in points:
    print(i, end=' ')



