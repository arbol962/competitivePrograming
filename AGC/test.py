# coding:utf-8
import sys
import math

n, m = map(int, input().split())
s = input()
t = input()
ans_str = ""
count_n = 1
count_m = 1

l = (n * m) // math.gcd (n, m)
ans_str_list = [""]*l 

if(s[0] == t[0]):
    ans_str_list[0] = s[0]

for i in range(l-1):
    if i+1 == count_n*(l/n)+1:
        ans_str_list[i+1] = s[count_n]
        count_n += 1
        #print("n done")
    if i+1 == count_m*(l/m)+1:
        ans_str_list[i+1] = t[count_m]
        count_m += 1
        #print("m done")
        
for j in range(l):
    if ans_str_list[j] == "":
        ans_str_list[j] = " "
    ans_str += ans_str_list[j]
ans = len(ans_str_list)

count_n = 1
count_m = 1
for k in range(l-1):
    if(k+1 <= len(s)):
        if k+1 == count_n*(l/n)+1:
            if(ans_str[k+1] != s[count_n]):
                ans = -1
                break
            count_n += 1
    if(k+1 <= len(t)):
        if k+1 == count_m*(l/m)+1:
            if(ans_str[k+1] != t[count_m]):
                ans = -1
                break
            count_m += 1
print("{}".format(ans))

