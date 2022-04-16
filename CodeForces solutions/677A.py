n,h = map(int,input().split())
hight = list(map(int,input().split()))
count = n

for i in range(n):
    if hight[i] > h:
        count+=1

print(count)