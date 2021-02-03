N,M = map(int,input().split())
AB = []
for i in range(M):
    AB.append(list(map(int,input().split())))
K = int(input())
CD = []
for i in range(K):
    CD.append(list(map(int,input().split())))

#print(AB)
#print(CD)

ans =0
#人がボールを置く位置をBit全探索
for i in range(1<<K):
    ball_position = []
    temp = 0
    #print(bin(i))
    for j in range(K):
        if i & (1<<j):
            ball_position.append(CD[j][0])
        else:
            ball_position.append(CD[j][1])
    #ボールの場所にあう条件を探す
    for k in AB:
        if k[0] in ball_position and k[1] in ball_position:
            temp += 1
    ans = max(ans,temp)
    
    #print(set(ball_position))
print(ans)