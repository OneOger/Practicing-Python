# Codeforces
# 469A

levels_amount = int(input())
little_x = list(map(int,input().split()))
little_y = list(map(int,input().split()))

del little_y[0]
del little_x[0]
little_x = set(little_x)
little_y = set(little_y)

if little_x | little_y == set(range(1, levels_amount + 1)):
    print('I become the guy.')
else:
    print('Oh, my keyboard!')








