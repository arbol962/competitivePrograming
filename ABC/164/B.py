a, b, c, d = list(map(int, input().split()))

for i in range(100):
    c -= b
    if c<=0:
        print("Yes")
        break
    a -= d
    if a<=0:
        print("No")
        break

