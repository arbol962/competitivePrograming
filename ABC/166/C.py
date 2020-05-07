n, m = list(map(int,input().split()))
h = list(map(int,input().split()))
ma = [0]*n
count = 0
for i in range(m):
    a, b = list(map(int,input().split()))
    ma[a-1] = max(ma[a-1],h[b-1])
    ma[b-1] = max(ma[b-1],h[a-1])

for i in range(n):
    if(ma[i]==0 or h[i]>ma[i]):
        count += 1
print(count)
