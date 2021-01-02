#N 個の正の整数 a0,a1,…,aN−1 と、正の整数 W とが与えられます。
#a0,a1,…,aN−1 の中から何個か選んで総和を W とすることができるかどうかを判定してください。
#input N W
#3 5

N,W = map(int,input().split())
r=0

for i in range(1<<N):
    s = 0
    for j in range(N):
        if i & (1<<j):
            s += (j+1)
    if s == W:
        r +=1

print(r)