# coding:utf-8
import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

N = int(input())
p = [int(input()) for i in range(N)]
p[p.index(max(p))] = max(p)/2
print(int(sum(p)))
