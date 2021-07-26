n,k = map(int,input().split())
h = list(map(int,input().split()))
dp = [10**5 * 10**4 for _ in range(n)]

dp[0] = 0

for i in range(1,n):
    for j in range(1,k+1):
        if (i-j) >= 0:
            tmp = dp[i-j] + abs(h[i]-h[i-j])
            dp[i] = min(dp[i], tmp)
    
print(dp[n-1])