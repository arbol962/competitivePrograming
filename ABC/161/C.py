n, k= list(map(int, input().split()))
if k<=n:
    if n%k == 0:
        print("0")
        exit()
amari = n%k
n = amari
while(True):
    new_n = abs(k-n)
    if new_n < n:
        n = new_n
    else :
        break
print(n)

