n = int(input())
h = list(map(int,input().split()))
dp = []

for i in range(n):
    dp.append(10**5 * 10**4)

dp[0] = 0

for j in range(1,n):
    tmp = dp[j-1] + abs(h[j]-h[j-1])
    dp[j] = min(dp[j], tmp)
    if j>1:
        tmp = dp[j-2] + abs(h[j]-h[j-2])
        dp[j] = min(dp[j], tmp)

print(dp[n-1])