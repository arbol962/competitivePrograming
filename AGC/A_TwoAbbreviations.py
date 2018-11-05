# coding:utf-8
import sys
import os
import fractions
f = open('A_input.txt', 'r')
sys.stdin = f

n, m = list(map(int, input().split()))
s = input()
t = input()
ans_str = ""
count_n = 1
count_m = 1

l = (n * m) // fractions.gcd (n, m)
ans_str_list = [""]*l 

if(s[0] == t[0]):
    ans_str_list[0] = s[0]
for i in range(l-1):
    #print("i+1 is : {}".format(i+1))
    #print("count_n*(l/n)+1 is : {}".format(count_n*(l/n)+1))
    if i+1 == count_n*(l/n)+1:
        #print("count_n is : {}".format(count_n))
        #print("len(ans_str_list) is : {}".format(len(ans_str_list)))
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

# 最後にチェック
count_n = 1
count_m = 1
if(s[0] != t[0]):
    ans = -1
else:
    for k in range(l-1):
        if(k+1 <= len(s)):
            if k+1 == count_n*(l/n)+1:
                if(ans_str[k+1] != s[count_n]):
                    #iprint("check n")
                    #print("k+1 is : {}".format(k+1))
                    #print("count_n is : {}".format(count_n))
                    ans = -1
                    break
                count_n += 1
        if(k+1 <= len(t)):
            if k+1 == count_m*(l/m)+1:
                if(ans_str[k+1] != t[count_m]):
                    #print("check m")
                    ans = -1
                    break
                count_m += 1
print("{}".format(ans))
