n,k = map(int,input().split())
round = list(map(int,input().split()))
z = []

for i in round:
    if i >= round[k-1] and i>0:
        z.append(i)

print(len(z))
