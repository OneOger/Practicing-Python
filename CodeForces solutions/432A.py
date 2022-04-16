n,k = map(int,input().split())
times = list(map(int,input().split()))
count = 0
limit = 5-k

for i in times:
    if i <= limit:
        count+=1

print(count//3)