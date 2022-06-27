# CodeForces
# 996A
# Solution without cicles and conditional operators.

num = int(input())
count = 0
count += num // 100
num %= 100
count += num // 20
num %= 20
count += num // 10
num %= 10
count += num // 5
num %= 5
count += num // 1
num %= 1
print(count)