# Codeforces
# 122A

number = int(input())
lucky = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
count = 0

for i in lucky:
    if number % i == 0:
        count += 1

if count > 0:
    print('YES')
else:
    print('NO')







