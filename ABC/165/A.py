import sys
k = int(input())
a, b = list(map(int, input().split()))
if a == b:
    if a%k == 0:
        print('OK')
    else:
        print('NG')
    sys.exit()
for i in range(a,b+1):
    if i%k == 0:
        print('OK')
        sys.exit()
print('NG')
