# coding:utf-8
import sys
import os
f = open('input_pa.txt', 'r')
sys.stdin = f

a = int(input())
b,c = map(int, input().split())
s = input()

print("{} {}".format(a+b+c, s))
