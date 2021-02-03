from itertools import combinations
N = int(input())
PL = [tuple(map(int,input().split())) for _ in range(N)]
PL.sort()
P = set(PL)
result =0
for a,b in combinations(P,2):
    if not ( b[1]-a[1]+b[0], b[1]-b[0]+a[0] ) in P:
        continue
    if not ( b[1]+a[0]-a[1], -b[0]+a[0]+a[1] ) in P:
        continue
    result = max(result, ( a[0]-b[0] ) ** 2 + ( a[1]-b[1] ) ** 2 )

print(result)
