# coding:utf-8
import sys
import os
f = open('input_coins.txt', 'r')
sys.stdin = f

a,b,c,x = map(int, [input() for i in range(4)])
ans = 0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if(x == 500*i + 100*j + 50*k):
                ans += 1
print("{}".format(ans))
