n = input()
count_small = 0
count_big = 0

for i in range(len(n)):
    if n[i] >= 'a' and n[i] <= 'z':
        count_small += 1
    else:
        count_big += 1

if count_small > count_big or count_small == count_big:
    n = n.lower()
    print(n)
else:
    n = n.upper()
    print(n)