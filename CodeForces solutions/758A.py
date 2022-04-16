n = int(input())
w = list(map(int,input().split()))
b = w[:]

for i in range(len(w)):
    if w[i] != max(w):
        w[i] = w[i] + (max(w)-w[i])
        
print(sum(w)-sum(b))