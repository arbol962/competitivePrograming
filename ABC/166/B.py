n, k = list(map(int, input().split()))

sunuke = [0]*n
for i in range(k):
    d = int(input())
    a = list(map(int,input().split()))
    for j in range(len(a)):
        sunuke[a[j]-1] += 1
print(sunuke.count(0))


