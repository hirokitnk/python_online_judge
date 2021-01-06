import itertools

N,M = map(int,input().split())
paths = [ input().replace(' ','') for _ in range(M) ]
routes = list( itertools.permutations(range(2,N+1)) )

answer = 0
for route in routes:
    lroute = list(route)
    lroute.insert(0,1)
    can = True
    for p_index in range( len(lroute) - 1 ):
        if lroute[p_index] < lroute[ p_index + 1 ]:
            path = str(lroute[ p_index]) + str(lroute[ p_index + 1 ])
        else:
            path = str(lroute[ p_index +1 ]) + str(lroute[ p_index])
        if not path in paths:
            can = False
            break
    if can:
        answer += 1

print(answer)