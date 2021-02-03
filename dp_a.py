N = int(input())
h = list(map(int,input().split()))
dp = [10**5 * 10**4 for _ in range(N)]

#配列の参照渡しで値を更新
def update_min(index,a,b):
    if a[index] > b:
        a[index] = b

dp[0] = 0
for i in range(1,N):
    update_min(i,dp,dp[i-1]+abs(h[i]-h[i-1]) )
    if i > 1:
        update_min(i,dp, dp[i-2]+abs(h[i]-h[i-2]) )

print(dp[N-1])