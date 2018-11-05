# coding:utf-8
import sys
import os
f = open('input_ss.txt', 'r')
sys.stdin = f

n, a, b = list(map(int, input().split()))
ans = 0

for i in range(n+1):
    str_i = str(i)
    array = list(map(int, list(str_i)))
    digit_sum = sum(array)
    if(a <= digit_sum and digit_sum <= b):
        ans += i
print("{}".format(ans))
