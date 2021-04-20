import bisect
n,m = map(int,input().split())
p = [int(input()) for i in range(n)]
p.append(0)
scores = []

for i in p:
    for j in p:
        scores.append(i+j)
scores = sorted(scores)
#print(scores)

res = 0
for s in scores:
    if s > m:
        break
    #print('----------')
    #print(f's={s}')
    #print(f'm-s={str(m-s)}')
    i = bisect.bisect_left(scores,m-s) - 1
    #print(f'i={i}')
    if i < 0:
        break
    res = max(res,s + scores[i])
    #print(f'res={res}')

print(res)