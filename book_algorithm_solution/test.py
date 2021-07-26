n = int(input())
a = int(input())
nums = list(map(int,input().split()))

res =0
for i in range(1<<n):
    sum = 0
    for j in range(n):
        if i & (1<<j):
            sum += nums[j]
    if sum == a:
        print(bin(i))
        res +=1
print(res)


"""
input
5
10
1 3 2 4 9
"""
