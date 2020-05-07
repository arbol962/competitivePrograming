n = int(input())
s = []
d = {}
for i in range(n):
    si = input()
    s.append(si)
    if si not in d:
        d[si] = 1
print(len(d))

