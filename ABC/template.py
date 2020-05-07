# coding:utf-8
import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# 入力が文字列
s = input().split()
a, b, c = input().split()

# 入力が数値(浮動小数点) 「A B C」
s = input().split()
n = list(map(int, input().split()))
n = list(map(float, input().split()))
a, b, c = list(map(int, input().split()))
a, b, c = list(map(float, input().split()))

# 最初に入力する個数(N)が与えられてそこからN個の入力が得られる場合
# N
# a1
# a2
# ...
# aN
N = int(input())
a = [input() for i in range(N)]

print("{} {}".format(, ))

# aとbの最大公約数(gcd)
from fractions import gcd
print(gcd(78627872,1798742872))

# 数字切り捨て
import  math
math.floor(x)
# 数字の切り上げ
ceil(x)

# 平方根
math.sqrt(x)

# copy.deepcopy
import copy
A=[1,2,3]
B=deepcopy(A)

# n^m
pow(n,m)

# n^mをpで割った余り
pow(n,m,p)
