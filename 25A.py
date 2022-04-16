n = int(input())
num = list(map(int, input().split()))
even = []
odd = []

for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

if len(even) < len(odd):
    print(num.index(*even) + 1)
else:
    print(num.index(*odd) + 1)