N,M = map(int,input().split())
k = []
for i in range(M):
    k.append(list(map(int,input().split())))
p = list(map(int,input().split()))
r = 0

for i in range(1<<N):
    can = True
    for j in range(M):
        k0 = k[j][0]
        on_s = 0
        for l in range(1,k0+1):
            if (i & (1<<k[j][l]-1)):
                on_s +=1
        if on_s % 2 != p[j]:
            can = False
    if can:
        r +=1
print(r)