n, m= list(map(int, input().split()))
a = list(map(int, input().split()))
sorted_a = sorted(a,reverse=True)
a_sum = sum(a)
if sorted_a[m-1] >= a_sum*1/(4*m):
    print("Yes")
else :
    print("No")

