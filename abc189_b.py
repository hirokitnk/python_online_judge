N,X = map(int,input().split())
total = 0
ans = 0
for i in range(N):
    V,P = map(int,input().split())
    total += V * P
    ans +=1
    if total > 100 * X:
        print(ans)
        exit()
print(-1)