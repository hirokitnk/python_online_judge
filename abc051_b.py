K,S = map(int,input().split())

ans = 0
flag = True
for i in range(K+1):
    for j in range(K+1):
        X = i
        Y = j
        Z = S - (X+Y)
        if Z >= 0 and Z <= K:
            ans +=1

print(ans)