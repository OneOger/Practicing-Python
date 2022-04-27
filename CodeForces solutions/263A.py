# CodeForces
# 263A


a = [list(map(int,input().split())) for i in range(5)]
for i in range(5):
    for j in range(5):
        if a[i][j] == 1:
            row = i
            col = j
print((abs(2 - row)+abs(2 - col)))






