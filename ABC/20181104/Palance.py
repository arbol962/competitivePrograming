# coding:utf-8
import sys
import os
f = open('input_p.txt', 'r')
sys.stdin = f

N = int(input())
T, A = list(map(int, input().split()))
H = list(map(int, input().split()))

abs_list = [abs(A - (T - i*0.006)) for i in H]
ans = abs_list.index(min(abs_list))

print("{} ".format(ans+1))
