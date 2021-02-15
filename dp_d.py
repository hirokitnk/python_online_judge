N,limit_W = map(int,input().split())
w = []
v = []
for i in range(N):
    a,b = map(int,input().split())
    w.append(a)
    v.append(b)
dp = []
for i in range(N+1):
    dp.append([0]*(limit_W+1))

for i in range(N):
    for cur_W in range(limit_W+1):
        # i番目を選ばない時(選べない)
        if cur_W < w[i]:
            # cur_Wつまり仮の重さ限界を、その品物の重さが超えてればそもそも選べない
            dp[i+1][cur_W] = dp[i][cur_W]
            print('Not Select')
        else:　#その品物単品で選んだ場合？
            dp[i+1][cur_W] = max(dp[i][cur_W],dp[i][cur_W - w[i]] + v[i])
            #iを選んだ場合の価値と、選ばない場合の価値の大きい方で更新
            print('Select')
        print(f'i+1,cur+W,w[i],v[i]={i+1},{cur_W},{w[i]},{v[i]}')
        for x in dp:
            print(x)

print(dp[N][limit_W])
