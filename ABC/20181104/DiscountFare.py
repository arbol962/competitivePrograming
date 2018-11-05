# coding:utf-8
import sys
import os
f = open('input_p.txt', 'r')
sys.stdin = f

x, y = list(map(int, input().split()))

print("{} ".format(int(x+y/2)))
