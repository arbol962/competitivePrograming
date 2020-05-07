# coding:utf-8
import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# 入力が文字列
D = int(input())
ans = "Christmas"
for i in range(25-D):
    ans += " Eve"
print(ans)
