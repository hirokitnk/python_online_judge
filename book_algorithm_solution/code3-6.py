n,k = map(int,input().split())
a = list(map(int,input().split()))

for i in range(1<<n):
    sum = 0
    for j in range(n):
        if i & (1<<j):
            sum += a[j]
    if sum == k:
        print("True")
        exit()

print("False")