N,K = list(map(int, input().split()))
h = [int(input()) for i in range(N)]
candidate = None
h.sort()
for i in range(N-K+1):
    tmp = h[i+K-1] - h[i]
    if candidate == None or tmp < candidate:
        candidate = tmp
print(candidate)
