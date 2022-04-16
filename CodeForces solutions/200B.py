n = int(input())
k = list(map(int,input().split()))
drinks = n*100
orange = 0

for i in k:
    orange+=i

print(orange/drinks*100)