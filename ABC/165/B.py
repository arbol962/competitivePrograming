import math
m = 100
count = 0
x = int(input())
while(1):
    m = math.floor(m*1.01)
    count += 1
    if m >= x:
        print(count)
        break
