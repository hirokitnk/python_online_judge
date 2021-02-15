n = int(input())
a = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n):
    dp[i+1] = max(dp[i],dp[i]+a[i])
    print(dp)

print(dp[n])