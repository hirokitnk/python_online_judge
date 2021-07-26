#!/usr/bin/env python3
import sys

N,W = map(int,input().split())
#N,W = [3,8]
wvlist = [list(map(int,input().split())) for _ in range(N)]
INF = 10**15
ans = INF

dp = [[INF for _ in range(N*1000+1)] for i in range(N+1)]
#dp = np.full((N+1,N*1000+1),INF)
dp[0][0] = 0
#print(dp)

for i in range(N):
    for v in range(N*1000+1):
        if v-wvlist[i][1]>=0:
            dp[i+1][v] = min(dp[i+1][v],dp[i][v-wvlist[i][1]]+wvlist[i][0])
        dp[i+1][v] = min(dp[i+1][v],dp[i][v])

for i in range(N*1000+1):
    if W >= dp[N][i]:
        ans = i

print("almost end of code")
print(dp)
print(ans)