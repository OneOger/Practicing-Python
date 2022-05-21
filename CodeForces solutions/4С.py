# Codeforces
# 4С

names = {}
database = []
sys_requests = int(input())

for i in range(0, sys_requests):
    a = input()
    if a not in names:
        names.setdefault(a, 0)
        database.append('OK')

    else:
        names[a] += 1
        names.setdefault(a + str(names[a]))
        database.append(a + str(names[a]))

print(*database, sep='\n')







