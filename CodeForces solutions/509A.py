# CodeForces
# 509A


n = int(input())
triangle = [[0]*n for i in range(n)]
max_triangle = []

for i in range(n):
    for j in range(n):
        triangle[0][j] = 1
        triangle[i][0] = 1

for i in range(1, n):
    for j in range(1, n):
        triangle[i][j] = triangle[i-1][j] + triangle[i][j-1]

for i in triangle:
    max_triangle.append(max(i))

print(max(max_triangle))









