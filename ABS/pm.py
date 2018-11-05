# coding:utf-8
import sys
f = open('input_pm.txt', 'r')
sys.stdin = f

s = input()

print("{}".format(s.count("1")))
