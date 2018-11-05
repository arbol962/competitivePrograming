# coding:utf-8
import sys
import os
f = open('input_so.txt', 'r')
sys.stdin = f

N = int(input())
a = list(map(int,input().split()))
ans = 0

while (1):
    for i in range(N):
        if(a[i]%2 == 0):
            a[i] = a[i]/2
        else:
            break
    if(i != N-1):
        break
    else:
        ans += 1

print("{}".format(ans))
