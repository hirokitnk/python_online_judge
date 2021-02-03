N = int(input())
A = list(map(int,input().split()))
result = 0

for l in range(N):
    #最小値を仮置きする
    x = A[l]
    for r in range(l,N):
        #rまでの位置で最小値を更新
        x = min(x,A[r])
        result = max(result,x*(r-l+1))

print(result)