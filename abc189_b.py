N,X = map(int,input().split())
total = 0
ans = 0
for i in range(N):
    #print(i)
    V,P = map(int,input().split())
    total += V * (P * 0.01)
    ans +=1
    #print(round(total,2))
    if round(total,2) > X:
        print(ans)
        exit()
print(-1)