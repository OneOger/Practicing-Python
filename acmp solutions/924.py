# acmp.ru
# 924

squares = [input() for i in range(4)]
count = 0

for i in range(3):
    for j in range(3):
        if squares[i][j] == squares[i][j+1]:
            if squares[i][j] == squares[i+1][j]:
                if squares[i][j+1] == squares[i+1][j+1]:
                    count += 1

print('No' if count > 0 else 'Yes')










