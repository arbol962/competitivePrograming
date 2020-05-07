# coding:utf-8
import sys
import os
import copy
f = open('input_id.txt', 'r')
sys.stdin = f

n, m = list(map(int, input().split()))
city_list = []

for i in range(m):
    pm, ym = list(map(int, input().split()))
    city_list.append([i,pm,ym])

city_count = {}
city = {}

for i,p,y in sorted(city_list, key=lambda x: x[2]):
    if not p in city_count:
        city_count[p] = 1
    else:
        city_count[p] += 1
    city[i,p] = city_count[p]

for i,p,y in city_list:
    print("{:0=6}{:0=6}".format(p, city[i,p]))





for i in range(m):
    cindex = len([1 for x in city_nums[city_list[i][0]-1] if x<city_list[i][1]])
    #cindex = sum(x <= city_list[i][j] for x in city_list[i])
    print("{:0=6}{:0=6}".format(city_list[i][0]-1, cindex+1))
