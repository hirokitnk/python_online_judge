N = int(input())
abc = []
for i in range(N):
    abc.append( list(map(int,input().split())) )
dp = [[0,0,0] for _ in range(N+1)]

for i in range(N):

    for j in range(3):
        for k in range(3):
            if i==0 or not j==k:
                dp[i+1][k] = max(dp[i+1][k],dp[i][j]+abc[i][k])
                #print(dp)

print(max(dp[N]))