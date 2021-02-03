N,K = map(int,input().split())
h = list(map(int,input().split()))
dp = [10**5 * 10**4 for _ in range(N)]

#配列の参照渡しで値を更新
def update_min(index,a,b):
    if a[index] > b:
        a[index] = b

dp[0] = 0
for i in range(N):
    for j in range(1,K+1):
        if i+j > N-1:
            continue
        update_min(i+j,dp,dp[i]+abs(h[i+j]-h[i]))

print(dp[N-1])