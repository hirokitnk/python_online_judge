n,m = map(int,input().split())

edge = []
for i in range(m):
    edge.append(list(map(int,input().split())))

ans = 0
for e in edge:
    print('--------------------')
    print(f'e={e}')
    isBridge = True
    for k in edge:
        print(f'k={k}')
        if e == k:
            continue
        if e[0] == k[0]:
            isBridge = False

    if isBridge:
        ans +=1

print(ans)