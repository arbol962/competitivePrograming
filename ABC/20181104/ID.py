# coding:utf-8
import sys
import os
import copy
f = open('input_id.txt', 'r')
sys.stdin = f

n, m = list(map(int, input().split()))
city_list = [[] for i in range(n)]
numbers = []

for i in range(m):
    pm, ym = list(map(int, input().split()))
    city_list[pm-1].append(ym)
city_list_copied = copy.deepcopy(city_list)

for i in range(n):
    city_list_copied[i].sort()
    for j in range(len(city_list[i])):
        cindex = sum(x <= city_list[i][j] for x in city_list[i])
        #cindex = city_list_copied[i].index(city_list[i][j])
        print("{:0=6}{:0=6}".format(i+1, cindex))
