N,Y = map(int,input().split())
X = []
for i in range(N+1):
    k = N
    k -= i
    if 10000*i > Y:
        break
    for j in range(k+1):
        l = k
        l -= j
        if (10000*i + 5000*j + 1000*l) == Y:
            X = [i,j,l]

if len(X) == 0:
    print("-1 -1 -1")
else:
    print(f'{X[0]} {X[1]} {X[2]}')
