import itertools
n,m,q = map(int,input().split())
a = [0]*q
b = [0]*q
c = [0]*q
d = [0]*q
for i in range(q):
    a[i],b[i],c[i],d[i] = map(int,input().split())
ans = 0
for A in itertools.combinations_with_replacement(range(1,m+1),n):
    print(list(range(1,m+1)))
    print(A)
    print()

    tmp = 0
    for i in range(q):
        if A[b[i]-1] - A[a[i]-1] == c[i]:
            tmp += d[i]
    ans = max(ans,tmp)
print(ans)
