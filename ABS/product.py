# coding:utf-8
import sys
import os
f = open('input_product.txt', 'r')
sys.stdin = f

a,b = list(map(int, input().split()))
if((a*b)%2 == 0):
    ans = "Even"
else:
    ans = "Odd"
print("{}".format(ans))
